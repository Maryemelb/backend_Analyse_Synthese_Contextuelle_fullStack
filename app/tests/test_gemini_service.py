import pytest

from app.services.gemini_service import sumerize
from unittest.mock import Mock
@pytest.fixture
def article():
    return "L intelligence artificielle connaît une croissance spectaculaire depuis les dernières années. Grâce aux avancées en deep learning et en puissance de calcul, les modèles deviennent capables de résoudre des problèmes auparavant réservés aux humains. Aujourd’hui, l’IA est utilisée dans de nombreux domaines tels que la santé, la finance, l’éducation, ou encore les transports autonomes. Des entreprises comme Google, OpenAI et Meta développent des systèmes toujours plus performants, capables de générer du texte, analyser des images, prédire des comportements, et même assister dans la prise de décision. Cependant, cette évolution rapide soulève aussi des questions importantes concernant la confidentialité, l’éthique, la transparence des modèles, et l’impact sur l’emploi. Les gouvernements et institutions internationales tentent d’établir des règles pour encadrer l’utilisation de ces technologies tout en encourageant l’innovation."


def test_sumerize(mocker):
     fake_response= mocker.Mock()
     fake_response.text= "resumed text"

     fake_client= mocker.Mock()
     mocker.patch('app.services.gemini_service.genai.Client', return_value= fake_client)

     fake_client.models.generate_content.return_value = fake_response
  
     result= sumerize(article, 'Ai')
     assert result == fake_response.text
     assert isinstance(result, str)
