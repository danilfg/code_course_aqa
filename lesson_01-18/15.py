import requests
from pprint import pprint
from faker import Faker

fake = Faker()

BASE_URL = 'https://api.bank.easyitlab.tech'


token_response = requests.post(
    f"{BASE_URL}/auth/login",
    json = {
        'email': 'gravitel0nd@gmail.com',
        'password': 'PlHmkUR1cNP9'
    },
    headers={
        'Content-Type': 'application/json'
    }
)
token = token_response.json().get('access_token')
pprint(dict(token_response.headers))


HEADERS = {
    "Authorization": f"Bearer {token}",
    'Content-Type': 'application/json'
}

def test_api_users_https():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS
    )
    print(response.text)

