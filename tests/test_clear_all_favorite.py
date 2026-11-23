import requests
from config.config import *

def test_clear_all_favorite():
    headers = {
        "Authorization": "Bearer token=dPCwgnLX3TLykvq4k1XJV8k7"
    }
    response = requests.delete(f"{base_url}favorites/clear_all",headers=headers)
    assert response.status_code == 204