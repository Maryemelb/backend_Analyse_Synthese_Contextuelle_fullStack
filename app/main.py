from database import Base
from fastapi import FastAPI
from database import engine
from sqlalchemy_utils import database_exists, create_database

app=FastAPI()

if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)

@app.get('/')
def initialize():
    return "app loaded!"
