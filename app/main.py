from fastapi import FastAPI
from app.routes import transaction_routes

app = FastAPI(title="API Bancária")

app.include_router(transaction_routes.router, prefix="/api")