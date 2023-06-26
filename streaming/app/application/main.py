import os
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def stream_audio():
    filenames = ["part1.mp3", "part2.mp3", "part3.mp3"]
    for filename in filenames:
        while not os.path.exists(filename):
            time.sleep(1)
        with open(filename, "rb") as f:
            while chunk := f.read(8192):
                yield chunk


@app.get("/audio")
async def audio_endpoint():
    return StreamingResponse(stream_audio(), media_type="audio/mpeg")
