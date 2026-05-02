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

def test_api_users_https():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS
    )

    assert response.url.startswith("https://")

def get_dashboard():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS
    )

    assert response.url.startswith("https://")
    return response.json()

def test_dashboard_employee_create():
    before = get_dashboard()

    payload = {
        'email': fake.email(),
        'full_name': fake.name()
    }

    requests.post(
        f"{BASE_URL}/students/employees",
        headers=HEADERS,
        json=payload
    )

    after = get_dashboard()

    assert after['employees_total'] >= before['employees_total']

def get_response_dashboard():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS
    )

    assert response.url.startswith("https://")
    return response

def test_rate_limiting():
    status = 200
    counter = 0
    while status != 429:
        status = get_response_dashboard().status_code
        counter += 1

    return counter

counter = test_rate_limiting()

print(counter)

