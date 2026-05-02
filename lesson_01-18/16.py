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



def create_employee():
    body = {
        'email': '',
        'full_name': fake.name()
    }

    created_employee = requests.post(
        f'{BASE_URL}/students/employees',
        json=body,
        headers=HEADERS
    )
    pprint(created_employee.status_code)
    pprint(created_employee.json())
    pprint(dict(created_employee.headers))
    assert created_employee.status_code == 200
    created_employee_json = created_employee.json()
    employee_id = created_employee_json.get('id')
    return employee_id

employee_id = create_employee()

get_created_employee = requests.get(
    f'{BASE_URL}/students/employees/{employee_id}',
    headers=HEADERS
)

# pprint(get_created_employee.json())

# get_created_employee_not_found = requests.get(
#     f'{BASE_URL}/students/employees/100000000',
#     headers=HEADERS
# )
# print(get_created_employee_not_found.status_code)