import requests
from config.config import *

def test_create_favorite_airport():
    headers = {
        "Authorization": "Bearer token=dPCwgnLX3TLykvq4k1XJV8k7"
    }
    payload = {
        "airport_id": "NRT",
        "note": "good airport"
    }
    response = requests.post(f"{base_url}favorites",headers=headers,json=payload)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201