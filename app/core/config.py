import os
import secrets
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage3"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 BACKEND (Stage 3)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    TELEX_WEBHOOK_URL: str = os.getenv("TELEX_WEBHOOK_URL")
    USER_NAME: str = os.getenv("USER_NAME")

settings = Settings()