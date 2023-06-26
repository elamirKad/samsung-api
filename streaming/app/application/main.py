from fastapi import FastAPI
from app.handlers.audio_handler import audio_router
from app.infrastructure.middleware.cors_middleware import middleware as cors_middleware

app = FastAPI(middleware=cors_middleware)

app.include_router(audio_router)
