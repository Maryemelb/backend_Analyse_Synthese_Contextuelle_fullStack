import os
import httpx
from dotenv import load_dotenv
import httpx
load_dotenv()

async def classify_article(article,labels):
   API_URL = os.getenv('HUGGING_FACE_API')
   headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
     }

   def query(payload):
      response =httpx.post(API_URL, headers=headers, json=payload, timeout=60.0)
      return response.json()
   output = query({
    "inputs": article,
    "parameters": {"candidate_labels": labels},
     })
   detected_category= max(output, key=lambda x :x["score"])

   return detected_category

async def predict_ton(resume: str):

  API_URL = os.environ['HUGGING_FACE_API_TON']
  headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
   }

  async def query(payload):
    async with httpx.AsyncClient(timeout=60.0) as client:
      response =await client.post(API_URL, headers=headers, json=payload)
      return response.json()

  output =await query({
    "inputs": resume,
    })
  predicted_ton= max(output[0], key=lambda x:x["score"])
  mapping= {
    "1 star": "negative",
    "2 stars": "negative",
    "3 stars": "neutral",
    "4 stars": "positive",
    "5 stars": "positive"
  }
  # mapping.get(predicted_ton['label'], "neutral")
  return mapping.get(predicted_ton['label'], "neutral")