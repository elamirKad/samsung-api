from fastapi import FastAPI
from handlers import genre_handler


app = FastAPI()

app.include_router(genre_handler.router, prefix="/genre", tags=["genre"])
