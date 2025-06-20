from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Account, Transaction
from .schemas import TransactionCreate

async def create_transaction(db: AsyncSession, account_id: int, transaction_data: TransactionCreate):
    if transaction_data.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")

    account = await db.get(Account, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if transaction_data.type == "withdraw" and account.balance < transaction_data.amount:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    if transaction_data.type == "withdraw":
        account.balance -= transaction_data.amount
    else:
        account.balance += transaction_data.amount

    transaction = Transaction(**transaction_data.dict(), account_id=account_id)
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction