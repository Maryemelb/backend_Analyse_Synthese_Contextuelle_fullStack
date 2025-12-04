import os
from fastapi import HTTPException
from app.models.user import users
import jwt
from dotenv import load_dotenv
load_dotenv()



def decode_token(token: str):
    payload= jwt.decode(token , os.getenv("jwt_secret"), algorithms=os.getenv("ALGORITHM"))
    if payload:
       return payload
def verify_user_in_db(user_in_token: str, db):
    user_in_db= db.query(users).filter(users.username == user_in_token).first()
    if not user_in_db:
       raise HTTPException(status_code=404, detail="Token not valid")
    return user_in_db.username
