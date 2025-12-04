from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from dotenv import load_dotenv
from pytest import Session

from app.dependencies import getdb
from app.models.user import users
from ..schemas.analysis_logs_schema import inserted_article
load_dotenv()

router= APIRouter(
    tags=['Main']
)
oauth_schema = OAuth2PasswordBearer(tokenUrl="token")
def decode_token(token: str):
    payload= {"username", jwt.decode(token , os.getenv("jwt_secret"), algorithms=os.getenv("HS256"))}
    if payload:
       return payload
def verify_user_in_db(user_in_token: str, db):
    user_in_db= db.query(users).filter(users.username == user_in_token).first()
    if not user_in_db:
       raise HTTPException(status_code=404, detail="Token not valid")
    return user_in_db.username
@router.post('/analyze')
def synthese(article: inserted_article,toke:str= Depends(oauth_schema), db:Session= Depends(getdb)):
    return article.article

