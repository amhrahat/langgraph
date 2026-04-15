from fastapi import FastAPI
from app.api import chat

app = FastAPI(title="LangGraph Agent API")

app.include_router(chat.router)