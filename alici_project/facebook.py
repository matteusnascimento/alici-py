import requests, os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('META_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')

def enviar_mensagem_facebook(texto):
    url = f"https://graph.facebook.com/v17.0/{PAGE_ID}/messages"
    payload = {"message": {"text": texto}, "recipient": {"id": "USER_ID"}, "messaging_type": "RESPONSE"}
    headers = {"Authorization": f"Bearer {TOKEN}"}
    return requests.post(url, json=payload, headers=headers).json()
