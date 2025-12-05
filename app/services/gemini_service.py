from google import genai
from google.genai import types
import os
import google.genai as genai
def sumerize(article="L’intelligence artificielle connaît une croissance spectaculaire depuis les dernières années. Grâce aux avancées en deep learning et en puissance de calcul, les modèles deviennent capables de résoudre des problèmes auparavant réservés aux humains. Aujourd’hui, l’IA est utilisée dans de nombreux domaines tels que la santé, la finance, l’éducation, ou encore les transports autonomes. Des entreprises comme Google, OpenAI et Meta développent des systèmes toujours plus performants, capables de générer du texte, analyser des images, prédire des comportements, et même assister dans la prise de décision. Cependant, cette évolution rapide soulève aussi des questions importantes concernant la confidentialité, l’éthique, la transparence des modèles, et l’impact sur l’emploi. Les gouvernements et institutions internationales tentent d’établir des règles pour encadrer l’utilisation de ces technologies tout en encourageant l’innovation.",category_predict="AI"):
    client = genai.Client(api_key=os.environ["GEMINI_API"])
    prompt= f"""
    Tu es un assistant expert en résumé.
    Tâche : résumer le texte ci-dessous.

    INFORMATIONS SUPPLÉMENTAIRES :
    - Catégorie HuggingFace : {category_predict}
    Texte à résumer :
    \"\"\"{article}\"\"\"
"""

    response = client.models.generate_content(
      model="gemini-2.5-flash",
      config=types.GenerateContentConfig(
        system_instruction="be as a seller an i want to buy something."),
      contents=prompt
    )
    return response.text if hasattr(response, "text") else None



