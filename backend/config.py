import os
from pydantic_settings import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    jwt_algorithm: str = "HS256"
    jwt_expiration_time: int = 3600  # 1 hour

    chroma_persist_directory: str = "./chroma_db"

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    # Dummy users for demo
    users: Dict[str, Dict[str, str]] = {
        "admin": {"password": "adminpass", "role": "Admin"},
        "employee": {"password": "employeepass", "role": "Employee"}
    }

settings = Settings()
