import requests
from config.config import *

def test_get_airport_id():
    response = requests.get(f"{base_url}airports/KIX")
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["data"]["id"] == "KIX"
    assert json_response["data"]["type"] == "airport"
    assert json_response["data"]["attributes"]["name"] == "Kansai International Airport"
    assert json_response["data"]["attributes"]["country"] == "Japan"
    assert json_response["data"]["attributes"]["city"] == "Osaka"
    assert json_response["data"]["attributes"]["iata"] == "KIX"
    assert json_response["data"]["attributes"]["icao"] == "RJBB"
    assert json_response["data"]["attributes"]["latitude"] == "34.427299"
    assert json_response["data"]["attributes"]["longitude"] == "135.244003"
    assert json_response["data"]["attributes"]["altitude"] == 26
    assert json_response["data"]["attributes"]["timezone"] == "Asia/Tokyo"