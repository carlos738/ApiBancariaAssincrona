from decimal import Decimal
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .database import Base, engine, get_session
from .models import User, Account, TransactionType
from .schemas import (
    UserCreate, UserOut, AccountCreate, AccountOut,
    TransactionCreate, TransactionOut, StatementOut, Token
)
from .auth import (
    get_password_hash, verify_password, create_access_token,
    get_current_user
)
from .crud import (
    get_user_by_username, create_user, create_account,
    get_account_by_number, list_transactions, apply_transaction
)


app = FastAPI(
    title="API Bancária Assíncrona",
    description="Gerencia depósitos, saques e extratos de contas correntes com JWT.",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    # Criar tabelas no banco em memória
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/auth/signup", response_model=UserOut, tags=["Autenticação"])
async def signup(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    existing = await get_user_by_username(session, payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed = get_password_hash(payload.password)
    user = await create_user(session, payload.username, hashed)
    await session.commit()
    return user


@app.post("/auth/login", response_model=Token, tags=["Autenticação"])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    user = await get_user_by_username(session, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    token = create_access_token(data={"sub": user.username})
    return Token(access_token=token)


@app.post("/accounts", response_model=AccountOut, tags=["Contas"])
async def create_account_endpoint(
    payload: AccountCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    existing = await get_account_by_number(session, current_user.id, payload.number)
    if existing:
        raise HTTPException(status_code=400, detail="Conta já existe para este usuário")
    account = await create_account(session, current_user.id, payload.number)
    await session.commit()
    return account


@app.post("/accounts/{number}/transactions", response_model=TransactionOut, tags=["Transações"])
async def create_transaction_endpoint(
    number: str,
    payload: TransactionCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    account = await get_account_by_number(session, current_user.id, number)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    try:
        tx = await apply_transaction(session, account, payload.type, Decimal(payload.amount))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    await session.commit()
    return tx


@app.get("/accounts/{number}/statement", response_model=StatementOut, tags=["Extrato"])
async def get_statement_endpoint(
    number: str,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    account = await get_account_by_number(session, current_user.id, number)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    transactions = await list_transactions(session, account.id)
    return StatementOut(account=account, transactions=transactions)











