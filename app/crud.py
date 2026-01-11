from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from .models import User, Account, Transaction, TransactionType


async def get_user_by_username(session: AsyncSession, username: str):
    result = await session.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()


async def create_user(session: AsyncSession, username: str, hashed_password: str) -> User:
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    await session.flush()
    return user


async def create_account(session: AsyncSession, user_id: int, number: str) -> Account:
    account = Account(user_id=user_id, number=number, balance=Decimal("0.00"))
    session.add(account)
    await session.flush()
    return account


async def get_account_by_number(session: AsyncSession, user_id: int, number: str):
    result = await session.execute(
        select(Account).where(Account.user_id == user_id, Account.number == number)
    )
    return result.scalar_one_or_none()


async def list_transactions(session: AsyncSession, account_id: int):
    result = await session.execute(
        select(Transaction).where(Transaction.account_id == account_id).order_by(Transaction.created_at.desc())
    )
    return result.scalars().all()


async def apply_transaction(session: AsyncSession, account: Account, tx_type: TransactionType, amount: Decimal) -> Transaction:
    if amount <= Decimal("0"):
        raise ValueError("Valor da transação deve ser positivo.")
    if tx_type == TransactionType.WITHDRAW and account.balance < amount:
        raise ValueError("Saldo insuficiente para saque.")
    if tx_type == TransactionType.DEPOSIT:
        account.balance = (Decimal(account.balance) + amount).quantize(Decimal("0.01"))
    else:
        account.balance = (Decimal(account.balance) - amount).quantize(Decimal("0.01"))
    tx = Transaction(account_id=account.id, type=tx_type, amount=amount)
    session.add(tx)
    await session.flush()
    return tx
