# to start the server: uvicorn app.main:app --reload
# installed pytest in root dir for endpoint testing
# decided to use sqlalchemy instead of sqlmodel in fastapi
# models folder defines sqlalchemy models(database tables)
# use pydantic_settings for loading settings class in core/config.py
# crud/ Contains Create, Read, Update, Delete operations that interact directly with the database. These functions operate on SQLAlchemy models.