# Plan to Fix 404 Error in Chatbot

## Information Gathered
- The project is a document-based chatbot with FastAPI backend and Next.js frontend.
- Backend routes include auth, documents, and chatbot.
- Current chatbot.py uses Ollama LLM and HuggingFace embeddings.
- Documents.py uses OpenAI embeddings, which requires an API key not defined in config.py, causing potential failures.
- The 404 error (with OpenRouter-style ID) suggests the code was modified to use OpenRouter, but the API key is missing or the model is unavailable.
- Config.py lacks OPENROUTER_API_KEY; needs to be added.
- No error handling in chatbot query endpoint for external API failures.

## Plan
- Update backend/config.py to include OPENROUTER_API_KEY environment variable.
- Update backend/routes/chatbot.py to use OpenRouter via ChatOpenAI for LLM, and add try-except error handling for API calls.
- Update backend/routes/documents.py to use HuggingFaceEmbeddings for consistency (removes OpenAI dependency).
- Update TODO.md to reflect completed changes for free chatbot setup.

## Dependent Files to Edit
- backend/config.py
- backend/routes/chatbot.py
- backend/routes/documents.py
- TODO.md

## Followup Steps
- Install/update Python dependencies if needed.
- Pull llama3 model using Ollama (from TODO).
- Test chatbot query functionality.
- Run application locally to verify no 404 errors.
- Ensure .env file includes OPENROUTER_API_KEY (user action required).

<ask_followup_question>
<question>Confirm if this plan addresses the 404 error by switching to OpenRouter with proper error handling. Do you have the OPENROUTER_API_KEY ready, or should I proceed with Ollama instead?</question>
</ask_followup_question>
