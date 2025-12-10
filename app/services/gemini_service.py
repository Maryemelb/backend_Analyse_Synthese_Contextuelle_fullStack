from google import genai
from google.genai import types
import os
import google.genai as genai
def sumerize(article,category_predict):
    
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
        system_instruction="be a good writer"),
      contents=prompt
    )
    return response.text if hasattr(response, "text") else None



