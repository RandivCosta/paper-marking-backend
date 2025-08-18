from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.db.database import create_db_and_tables

app = FastAPI()

# execute the folling code once to create database if not exists.
# create_db_and_tables()
# print("Database tables created.")

app.include_router(api_router)

@app.get("/")
async def read_root():
    return{ "message": "Welcome to the OCR project API!" }