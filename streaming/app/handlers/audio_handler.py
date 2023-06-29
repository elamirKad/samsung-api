import os
import time
import glob
import asyncio
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.domain.services.audio_service import AudioService

audio_router = APIRouter()


async def stream_audio(directory: str):
    tries = 0
    while True:
        files = sorted(glob.glob(f"{directory}/*.mp3"), key=lambda name: int(name.split('/')[-1].split('.')[0]))
        if len(files) == 0:
            if tries > 10:
                break
            tries += 1
            await asyncio.sleep(1)
            continue

        for file in files:
            previous_size = -1
            while True:
                size = os.stat(file).st_size
                if size == previous_size:
                    break
                previous_size = size
                await asyncio.sleep(1)

            with open(file, "rb") as f:
                while chunk := f.read(8192):
                    yield chunk
        break


@audio_router.get("/audio/{id}")
async def audio_endpoint(id: int, audio_service: AudioService = Depends()):
    audio = await audio_service.get(id)
    return StreamingResponse(stream_audio(audio.path), media_type="audio/mpeg")
