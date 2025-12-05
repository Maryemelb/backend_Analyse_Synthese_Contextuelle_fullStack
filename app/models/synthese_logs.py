from sqlalchemy import Column, Integer, String, Float,Text

from ..database import Base

class synthese_logs(Base):
    __tablename__= "synthese_logs"
    id= Column(Integer, primary_key=True)
    article= Column(String, nullable=False)
    category_predict=Column(String)
    score=Column(Float)
    resume=Column(String)
    ton= Column(Text)
