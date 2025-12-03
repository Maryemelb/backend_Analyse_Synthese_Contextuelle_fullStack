from app.database import Base,engine
from fastapi import FastAPI
from sqlalchemy_utils import database_exists, create_database
from .routes.register import router as signup_router
app=FastAPI()

if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)


app.include_router(signup_router)
