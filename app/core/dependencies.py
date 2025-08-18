# contains reusable dependency injection functions, such as getting a database session or verifying authentication tokens
from typing import Annotated, Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal

def get_db() -> Generator:
    """Dependency to get a database session"""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Alias for easier use in routes
# Lets you attach extra metadata to a type hint
# FastAPI uses this to know both the type and the dependency
get_db_session = Annotated[Session, Depends(get_db)]