from fastapi import APIRouter, Depends, HTTPException
from backend.routes.auth import get_current_user
from backend.models import User, UserRole, QueryRequest, QueryResponse
from backend.config import settings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import chromadb

router = APIRouter()


def get_vectorstore():
    client = chromadb.PersistentClient(path=settings.chroma_persist_directory)
    return Chroma(
        client=client,
        collection_name="documents",
        embedding_function=OpenAIEmbeddings(openai_api_key=settings.openai_api_key),
    )


def get_qa_chain():
    vectorstore = get_vectorstore()
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=settings.openai_api_key)
    return RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
    )


@router.post("/query", response_model=QueryResponse)
async def query_chatbot(
    request: QueryRequest, current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.EMPLOYEE:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    # qa_chain = get_qa_chain()
    # response = qa_chain.run(request.query)
    response = f"Mock response to query: {request.query}"
    return QueryResponse(response=response)
