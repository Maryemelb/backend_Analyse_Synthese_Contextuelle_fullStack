from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from dotenv import load_dotenv
from pytest import Session

from app.dependencies import getdb
from app.models.user import users
from app.services.auth_service import decode_token, verify_user_in_db
from app.services.hugging_face_service import classify_article
from ..schemas.analysis_logs_schema import inserted_article
load_dotenv()

router= APIRouter(
    tags=['Main']
)
oauth_schema = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/analyze')
async def synthese(article: inserted_article,token:str= Depends(oauth_schema), db:Session= Depends(getdb)):
    payload= decode_token(token)
    if not verify_user_in_db(payload["username"],db):
       raise HTTPException(status_code=403, detail="User not authorized")
    output = await classify_article(article.article,article.categories)
    return max(output, key=lambda x :x["score"])
