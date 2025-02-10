from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

if not os.getenv("SECRET_KEY"):
    load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
EXP_TIME_MIN = int(os.getenv("EXP_TIME_MIN"))

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def encode_token(payload: dict) -> str:
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes = EXP_TIME_MIN)
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth_scheme)]) -> dict:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def get_current_user(token: str = Depends(oauth_scheme)) -> dict:
    return decode_token(token)