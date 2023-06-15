from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from auth_service import create_random_code, authenticate_user
from auth_token import get_current_user
from models import User
from database import get_db

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/check")


class AuthRequest(BaseModel):
    email: str
    code: str


@app.post("/auth/")
async def auth(email: str, db: Session = Depends(get_db)):
    await create_random_code(db, email)
    return {"message": "Code created and sent by email."}


@app.post("/auth/check/")
async def auth_check(auth_request: AuthRequest, db: Session = Depends(get_db)):
    token = await authenticate_user(db, auth_request.email, auth_request.code)
    return {"access_token": token}


@app.get("/profile/")
async def profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = await get_current_user(token)
    user_email = token_data.user_email
    user = db.query(User).filter(User.email == user_email).first()
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return user



@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "unhealthy", "detail": str(e)}
