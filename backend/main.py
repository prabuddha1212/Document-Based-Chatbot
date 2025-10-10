from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.documents import router as documents_router
from routes.chatbot import router as chatbot_router
import chromadb
from config import settings

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Chroma
client = chromadb.PersistentClient(path=settings.chroma_persist_directory)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(documents_router, prefix="/documents", tags=["documents"])
app.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Chatbot API"}
