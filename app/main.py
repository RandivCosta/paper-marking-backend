from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import api_router
from app.db.database import create_db_and_tables

app = FastAPI()

# execute the folling code once to create database if not exists.
# create_db_and_tables()
# print("Database tables created.")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the list of allowed origins.
    allow_credentials=True,  # Allows cookies and credentials to be sent.
    allow_methods=["*"],  # Allows all standard HTTP methods (GET, POST, PUT, DELETE, etc.).
    allow_headers=["*"],  # Allows all headers in the request.
)

app.include_router(api_router)

@app.get("/")
async def read_root():
    return{ "message": "Welcome to the OCR project API!" }