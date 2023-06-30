from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.handlers.audio_handler import audio_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio_router)
