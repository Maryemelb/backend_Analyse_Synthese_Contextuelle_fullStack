import pytest

from app.services.hugging_face_service import classify_article, predict_ton 


@pytest.fixture
def article():
    return 'Like most entrepreneurs, I struggled through my first year of building a business.I launched my first product without having any idea who I would sell it to. (Big surprise, nobody bought it.) I reached out to important people, mismanaged expectations, made stupid mistakes, and essentially ruined the chance to build good relationships with people I respected. I attempted to teach myself how to code, made one change to my website, and deleted everything I had done during the previous three months.'

@pytest.mark.anyio
async def test_classify_article(article):
    categories= ['business','monney', 'challenge' ]
    detected_cat=await classify_article(article, categories)
    assert detected_cat is not None
    assert isinstance(detected_cat['label'], str)
    assert isinstance(detected_cat['score'], float)


@pytest.mark.anyio
async def test_predict_ton():
    resume= 'L’auteur raconte avoir rencontré de nombreuses difficultés lors de sa première année d’entrepreneuriat : lancement d’un produit sans cible définie, erreurs dans la gestion des relations avec des personnes influentes, mauvais choix stratégiques, et même la perte de plusieurs mois de travail en essayant d’apprendre à coder et en modifiant maladroitement son site web.'
    predicted_ton= await predict_ton(resume)
    assert predicted_ton
    assert isinstance(predicted_ton, str)


