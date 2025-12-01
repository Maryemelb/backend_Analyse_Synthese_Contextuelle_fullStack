from database import Base
from sqlalchemy import Column, Integer, String, Float

class synthese_logs(Base):
    __tablename__= "synthese_logs",
    id= Column(Integer, primary_key=True)
    article= Column(String, nullable=False)
    category_predit=Column(String)
    score=Column(Float)
    resume=Column(String)
    ton= Column(String)
