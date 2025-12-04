from pydantic import BaseModel

class inserted_article(BaseModel):
    article: str
    categories: list
    
