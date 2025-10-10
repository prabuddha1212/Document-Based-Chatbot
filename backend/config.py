import os
from pydantic_settings import BaseSettings
from typing import Dict


class Settings(BaseSettings):
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    jwt_algorithm: str = "HS256"
    jwt_expiration_time: int = 3600  # 1 hour

    chroma_persist_directory: str = "./chroma_db"

    # Model configuration for LLM
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    model_name: str = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    # Dummy users for demo
    users: Dict[str, Dict[str, str]] = {
        "admin": {"password": "adminpass", "role": "Admin"},
        "employee": {"password": "employeepass", "role": "Employee"},
    }


settings = Settings()
