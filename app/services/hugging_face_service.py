import os
import httpx
from dotenv import load_dotenv
load_dotenv()

async def classify_article(article,labels):
   API_URL = os.getenv('HUGGING_FACE_API')
   headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
     }

   def query(payload):
      response =httpx.post(API_URL, headers=headers, json=payload)
      return response.json()
   output = query({
    "inputs": article,
    "parameters": {"candidate_labels": labels},
     })
   return output