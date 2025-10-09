from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from backend.routes.auth import get_current_user
from backend.models import User, UserRole
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
import os
import shutil
from backend.config import settings
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

router = APIRouter()


def get_vectorstore():
    client = chromadb.PersistentClient(path=settings.chroma_persist_directory)
    return Chroma(
        client=client,
        collection_name="documents",
        embedding_function=OpenAIEmbeddings(openai_api_key=settings.openai_api_key),
    )


def load_document(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith(".md"):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type")
    return loader.load()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...), current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    file_path = f"../docs/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # documents = load_document(file_path)
    # vectorstore = get_vectorstore()
    # vectorstore.add_documents(documents)

    return {"message": "Document uploaded successfully"}


@router.delete("/delete/{doc_id}")
async def delete_document(doc_id: str, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    # Assuming doc_id is the filename or something; need to map properly
    # For simplicity, delete from vectorstore by id
    vectorstore = get_vectorstore()
    vectorstore.delete([doc_id])

    return {"message": "Document deleted successfully"}
