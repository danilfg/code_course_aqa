import requests
import pytest

@pytest.fixture
def base_url():
    base_url = 'https://api.bank.easyitlab.tech'
    return base_url

@pytest.fixture
def access_token(base_url):
    token_response = requests.post(
        f"{base_url}/auth/login",
        json={
            'email': 'gravitel0nd@gmail.com',
            'password': 'PlHmkUR1cNP9'
        },
        headers={
            'Content-Type': 'application/json'
        }
    )

    assert token_response.status_code == 200, ""
    token_response_json = token_response.json()

    assert isinstance(token_response_json, dict)

    access_token = token_response_json.get('access_token')
    assert access_token, "token not found"
    return access_token

@pytest.fixture
def auth_headers(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }
    return headers