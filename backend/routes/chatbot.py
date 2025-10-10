from fastapi import APIRouter, Depends, HTTPException
from backend.routes.auth import get_current_user
from backend.models import User, UserRole, QueryRequest, QueryResponse
from backend.config import settings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb

router = APIRouter()


def get_vectorstore():
    client = chromadb.PersistentClient(path=settings.chroma_persist_directory)
    return Chroma(
        client=client,
        collection_name="documents",
        embedding_function=HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )


def get_qa_chain():
    vectorstore = get_vectorstore()
    llm = Ollama(model=settings.model_name)
    return RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
    )


@router.post("/query", response_model=QueryResponse)
async def query_chatbot(
    request: QueryRequest, current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.EMPLOYEE:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    qa_chain = get_qa_chain()
    response = qa_chain.run(request.query)
    return QueryResponse(response=response)
