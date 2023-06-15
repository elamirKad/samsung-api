import os
import random
import string
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from datetime import datetime, timedelta
from fastapi import HTTPException
from auth_token import create_access_token
from mail import send_code
from models import User, Code


async def create_random_code(db: Session, email: str):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    new_code = Code(email=email, code=code)
    db.add(new_code)
    db.commit()

    await send_code(email, code)


async def authenticate_user(db: Session, email: str, code: str):
    ten_minutes_ago = datetime.now() - timedelta(minutes=10)
    code_obj = db.query(Code).filter(and_(Code.email == email, Code.code == code, Code.created_at > ten_minutes_ago)).first()

    if not code_obj:
        raise HTTPException(status_code=400, detail="Invalid code or email, or the code has expired.")

    user = db.query(User).filter(User.email == email).first()

    if not user:
        user = User(email=email)
        db.add(user)
        db.commit()

    access_token = await create_access_token(data={"sub": str(user.email), "user_id": str(user.id)})

    return access_token
