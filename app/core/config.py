# defines application wide settings
# Pydantic Settings provides optional Pydantic features for loading a settings or config class from environment variables or secrets files.
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import Session

class Settings(BaseSettings):
    PROJECT_NAME: str = "Paper Marking Server"
    API_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Backend for Paper Marking Project with OCR functionalities, user authentication and dashboard project management."
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "mnsVrc#" # CHANGE THIS IN PRODUCTION
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database settings
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()