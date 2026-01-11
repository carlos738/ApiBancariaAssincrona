from typing import List, Optional
from pydantic import BaseModel, Field, condecimal
from datetime import datetime
from .models import TransactionType


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: Optional[str] = None


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=64)
    password: str = Field(min_length=6, max_length=128)


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class AccountCreate(BaseModel):
    number: str = Field(min_length=3, max_length=32)


class AccountOut(BaseModel):
    id: int
    number: str
    balance: condecimal(max_digits=12, decimal_places=2)

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    type: TransactionType
    amount: condecimal(max_digits=12, decimal_places=2)  # validação de precisão


class TransactionOut(BaseModel):
    id: int
    type: TransactionType
    amount: condecimal(max_digits=12, decimal_places=2)
    created_at: datetime

    class Config:
        from_attributes = True


class StatementOut(BaseModel):
    account: AccountOut
    transactions: List[TransactionOut]
