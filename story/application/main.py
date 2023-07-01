from fastapi import FastAPI
from handlers import genre_handler, topic_handler, story_handler, choice_handler, page_handler


app = FastAPI()

app.include_router(genre_handler.router, prefix="/genre", tags=["genre"])
app.include_router(topic_handler.router, prefix="/topic", tags=["topic"])
app.include_router(story_handler.router, prefix="/story", tags=["story"])
app.include_router(choice_handler.router, prefix="/choice", tags=["choice"])
app.include_router(page_handler.router, prefix="/page", tags=["page"])
