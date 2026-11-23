import requests
from config.config import *
from data.data import LOGIN_DATA

def test_post_token_using_valid_data():
    user = LOGIN_DATA["valid_user"]
    params = {
        "email": LOGIN_DATA["valid_user"]["email"],
        "password": LOGIN_DATA["valid_user"]["password"]
    }
    response = requests.post(f"{base_url}tokens",params=params)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["token"] is not None
    print(response.status_code)
    print(response.text)
    
def test_post_token_using_invalid_email():
    params = {
        "email": "taman123@gmail.com",
        "password": "r1zk1mp12345!"
    }
    response = requests.post(f"{base_url}tokens",params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 401