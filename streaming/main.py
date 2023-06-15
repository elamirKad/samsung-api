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

def stream_audio():
    with open("_neurosama - I don't want to be an engineer.mp3", "rb") as f:
        while chunk := f.read(8192):
            yield chunk

@app.get("/audio")
def audio_endpoint():
    return StreamingResponse(stream_audio(), media_type="audio/mpeg")
