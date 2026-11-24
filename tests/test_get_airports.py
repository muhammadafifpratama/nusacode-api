import requests
from config.config import *

def test_get_airport_id():
    response = requests.get(f"{base_url}airports")
    assert response.status_code == 200
    # print(response.status_code)
    # print(response.text)
    json_response = response.json()
    print("nama airportnya adalah = " + json_response["data"][0]["attributes"]["name"])