import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from os import getenv


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def decode_access_token(token: str = Depends(oauth2_scheme)) -> Optional[int]:
    """Verify and decode a JWT."""
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
