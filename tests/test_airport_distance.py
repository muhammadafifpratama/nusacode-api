import requests
from config.config import *

def test_airport_distance():
    payload = {
        "from" : "HLP",
        "to" : "NRT"
    }
    response = requests.post(f"{base_url}/airports/distance",json=payload)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)