from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

middleware = [
    CORSMiddleware(
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]
