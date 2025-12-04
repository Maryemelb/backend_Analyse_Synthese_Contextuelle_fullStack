from app.database import Base,engine
from fastapi import FastAPI
from sqlalchemy_utils import database_exists, create_database
from .routes.register import router as signup_router
from .routes.login import router as loging_router
from .routes.synthese import router as resume_router

app=FastAPI()

if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)


app.include_router(signup_router)
app.include_router(loging_router)
app.include_router(resume_router)