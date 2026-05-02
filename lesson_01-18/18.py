from pprint import pprint

import requests
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

assert token_response.status_code == 200, ""
token_response_json = token_response.json()

assert isinstance(token_response_json, dict)

token = token_response_json.get('access_token')
assert token,"token not found"

HEADERS = {
    "Authorization": f"Bearer {token}",
    'Content-Type': 'application/json'
}

# params = {
#     "status": "CLOSED"
# }
#
# clients = requests.get(
#     f'{BASE_URL}/students/clients',
#     params=params,
#     headers=HEADERS
# )
#
# clients_json = clients.json()
#
#
#
# pprint(len(clients_json))
# pprint(clients_json)

def test_status_active():
    check_status = 'CLOSED'

    params = {
        "status": check_status
    }
    clients = requests.get(
        f'{BASE_URL}/students/clients',
        params=params,
        headers=HEADERS
    )

    clients_json = clients.json()

    for client in clients_json:
        assert client['status'] == check_status
    print("test success")



test_status_active()