from app.database import Base,engine
from fastapi import FastAPI
from sqlalchemy_utils import database_exists, create_database
from .routes.register import router as signup_router
from .routes.login import router as loging_router
from .routes.synthese import router as resume_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins=[
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)


app.include_router(signup_router)
app.include_router(loging_router)
app.include_router(resume_router)
