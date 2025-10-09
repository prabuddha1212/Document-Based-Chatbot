# TODO List for Document-Based Chatbot

## Step 1: Define use case ✅
- Use case: Company documents (policies, manuals)
- User roles: Admin (upload/delete docs), Employee (query chatbot)
- Privacy: Role-based access
- Document types: PDF, DOCX, Markdown

## Step 2: Set up project structure and sample docs ✅
- Create backend/, frontend/, docs/ directories
- Set up Python venv and install backend deps
- Create Next.js frontend
- Add sample docs (sample_policy.md, sample_manual.md)
- Create .env, .gitignore, README.md

## Step 3: Select tech stack ✅
- Backend: FastAPI, LangChain, Chroma, OpenAI
- Frontend: Next.js

## Step 4: Build backend ✅
- Create FastAPI app structure (main.py, config.py, models.py, routes/)
- Implement JWT authentication for login
- Create user models with roles (Admin, Employee)
- Implement document upload endpoint (Admin only)
- Implement document delete endpoint (Admin only)
- Integrate document loaders for PDF, DOCX, MD
- Set up Chroma vector database
- Create query endpoint for chatbot (Employee only)

## Step 5: Implement RAG pipeline ✅
- Use LangChain to create retrieval chain
- Embed documents using OpenAI embeddings
- Store embeddings in Chroma
- Generate responses using OpenAI GPT-4o

## Step 6: Build frontend ✅
- Create login page with JWT auth
- Create admin dashboard for upload/delete docs
- Create employee chat interface
- Integrate with backend APIs
- Add UI for file uploads and chat

## Step 7: Test and evaluate ✅
- Test authentication and role-based access ✅
- Test document upload and processing ✅
- Test chatbot queries for accuracy ✅
- Evaluate response quality ✅

## Step 8: Deploy ✅
- Create Dockerfiles for backend and frontend
- Set up docker-compose.yml
- Updated frontend to use environment variable for API URL
- Deploy backend to Heroku using Dockerfile
- Deploy frontend to Vercel, set NEXT_PUBLIC_API_BASE_URL to backend URL

## Step 9: Security and maintenance
- Implement PII detection in documents
- Add logging for queries and uploads
- Set up monitoring and alerts
- Regular security audits
