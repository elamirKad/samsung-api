import os
import time
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

audio_router = APIRouter()


async def stream_audio():
    filenames = ["part1.mp3", "part2.mp3", "part3.mp3"]
    for filename in filenames:
        while not os.path.exists(filename):
            time.sleep(1)
        with open(filename, "rb") as f:
            while chunk := f.read(8192):
                yield chunk


@audio_router.get("/audio")
async def audio_endpoint():
    return StreamingResponse(stream_audio(), media_type="audio/mpeg")
