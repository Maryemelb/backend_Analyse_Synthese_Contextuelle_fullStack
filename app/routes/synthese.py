from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.dependencies import getdb
from app.models.synthese_logs import synthese_logs
from app.models.user import users
from app.services.auth_service import decode_token, verify_user_in_db
from app.services.gemini_service import sumerize
from app.services.hugging_face_service import classify_article, predict_ton
from ..schemas.analysis_logs_schema import inserted_article
load_dotenv()

router= APIRouter(
    tags=['Main']
)


@router.post('/analyze')
async def synthese(article: inserted_article,request:Request, db:Session= Depends(getdb)):
    token= request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=401, detail="Token not found")
    payload= decode_token(token)
    if not verify_user_in_db(payload["username"],db):
       raise HTTPException(status_code=403, detail="User not authorized")
    
    detected_category = await classify_article(article.article,article.categories)
    text=  sumerize(article.article,detected_category)
    ton=await predict_ton(text)

    synthes_db = synthese_logs(
    article=article.article,
    category_predict=detected_category["label"],
    score=detected_category["score"],
    resume=text,
    ton=ton
   )  
    db.add(synthes_db)
    db.commit()
    db.refresh(synthes_db)

    return {
        "detected_category": detected_category["label"],
        "score ": detected_category["score"],
        "summurized_text": text,
        "predicted_ton": ton
        }
