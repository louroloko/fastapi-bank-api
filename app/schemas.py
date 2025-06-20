from pydantic import BaseModel
from typing import List
from datetime import datetime

class TransactionCreate(BaseModel):
    type: str
    amount: float

class TransactionOut(BaseModel):
    id: int
    type: str
    amount: float
    timestamp: datetime

    class Config:
        orm_mode = True

class AccountOut(BaseModel):
    id: int
    balance: float
    transactions: List[TransactionOut] = []