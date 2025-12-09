import pytest

from app.services.hugging_face_service import classify_article, predict_ton 
from unittest.mock import Mock, AsyncMock

@pytest.fixture
def article():
    return 'pytest-mock est un package de pytest qui facilite la création de mocks (faux objets) pendant les tests.", ["pytest-mock'

@pytest.mark.anyio
async def test_classify_article(mocker):
  fake_response= [
     {"label": "pytest-mock", "score":0.8},
     {"label": "marketing", "score":0.3}
  ]
  fake=mocker.Mock()
  fake.status_code = 200
  fake.json.return_value= fake_response

  mocker.patch('app.services.hugging_face_service.httpx.post', return_value=fake)
  result = await classify_article(article, ["marketing","pytest-mock"])
  assert result["label"] == "pytest-mock"
  assert result["score"] == 0.8



@pytest.mark.anyio
async def test_predict_ton(mocker):
   fake_response= [[
      {"label": "5 stars", "score":0.7},
      {"label": "3 stars", "score":0.3},
      {"label": "1 star", "score":0.1}
   ]]
  

   make_mocker_post= mocker.patch("app.services.hugging_face_service.httpx.post")
   make_mocker_post.return_value.json.return_value= fake_response
   
   resume= 'L auteur raconte avoir rencontré de nombreuses difficultés lors de sa première année dentrepreneuriat'
   result=await predict_ton(resume)
   assert result== "positive"

