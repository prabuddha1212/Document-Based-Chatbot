from pydantic import BaseModel
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "Admin"
    EMPLOYEE = "Employee"

class User(BaseModel):
    username: str
    password: str
    role: UserRole

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Document(BaseModel):
    id: str
    filename: str
    content: str

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str
