import os
import hashlib
from pydantic_settings import BaseSettings
from typing import Dict


class Settings(BaseSettings):
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    jwt_algorithm: str = "HS256"
    jwt_expiration_time: int = 3600  # 1 hour

    chroma_persist_directory: str = "./chroma_db"

    # Model configuration for LLM
    openai_api_key: str = os.getenv("OPENROUTER_API_KEY")
    model_name: str = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    # Dummy users for demo
    users: Dict[str, Dict[str, str]] = {
        "admin": {
            "password": "713bfda78870bf9d1b261f565286f85e97ee614efe5f0faf7c34e7ca4f65baca",
            "role": "Admin",
        },
        "employee": {
            "password": "dad7d3ee2c8090d4af3196c2d47ea2f9ef297504ac6b21e587fb9bfff6c4069b",
            "role": "Employee",
        },
    }


settings = Settings()
