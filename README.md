# Document-Based Chatbot

A RAG-based chatbot for company documents.

## Tech Stack

- Backend: FastAPI, LangChain, Chroma, OpenAI

- Frontend: Next.js

## Setup

1. Backend: cd backend && venv\Scripts\activate && uvicorn main:app --reload

2. Frontend: cd frontend && npm run dev

## Local Development with Docker

Run `docker-compose up` to start both backend and frontend in containers.

## Deployment

### Backend to Heroku

1. Install Heroku CLI.
2. `heroku create your-app-name`
3. `heroku container:login`
4. `heroku container:push web -a your-app-name`
5. `heroku container:release web -a your-app-name`
6. Set environment variables: `heroku config:set OPENAI_API_KEY=your_key JWT_SECRET_KEY=your_secret`

### Frontend to Vercel

1. Push the repository to GitHub.
2. Connect the GitHub repo to Vercel.
3. In Vercel dashboard, set environment variable `NEXT_PUBLIC_API_BASE_URL` to your Heroku backend URL (e.g., https://your-app-name.herokuapp.com).
4. Deploy.
