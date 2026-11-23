import requests
from config.config import *

def test_create_favorite_airport():
    headers = {
        "Authorization": "Bearer token=dPCwgnLX3TLykvq4k1XJV8k7"
    }
    payload = {
        "note": "sudah di update nih",
    }
    response = requests.patch(f"{base_url}/favorites/49000",headers=headers,json=payload)
    assert response.status_code == 404
    print(response.status_code)
    print(response.text)