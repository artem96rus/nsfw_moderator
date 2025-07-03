import os
import base64
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
if not HUGGINGFACE_API_KEY:
  raise RuntimeError('HUGGINGFACE_API_KEY is not set')

@app.post('/moderate')
async def moderate_image(file: UploadFile = File(...)):
  if file.content_type not in ['image/jpeg', 'image/png']:
    raise HTTPException(status_code=400, detail='Only .jpg or .png files are supported')

  img_bytes = await file.read()
  b64_img = base64.b64encode(img_bytes).decode('utf-8')
  data = { 'inputs': f'data:{file.content_type};base64,{b64_img}' }

  headers = {
    'Authorization': f'Bearer {HUGGINGFACE_API_KEY}',
    'Content-Type': 'application/json'
  }

  url = 'https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection'

  try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(' Hugging Face API error:', str(e))
    raise HTTPException(status_code=500, detail='Hugging Face API error')

  result = response.json()
  print('API Response:', result)

  nsfw_score = 0.0
  for item in result:
    if item['label'].lower() == 'nsfw':
      nsfw_score = item['score']
      break

  if nsfw_score > 0.7:
    return JSONResponse(content={'status': 'REJECTED', 'reason': 'NSFW content'})
  return {'status': 'OK'}