from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from ..schemas import TransactionCreate, TransactionOut
from ..crud import create_transaction

router = APIRouter()

@router.post("/accounts/{account_id}/transactions", response_model=TransactionOut)
async def add_transaction(account_id: int, transaction: TransactionCreate, db: AsyncSession = Depends(SessionLocal)):
    return await create_transaction(db, account_id, transaction)