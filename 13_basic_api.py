"""
mobile app > backend service > backend processing > mobile app
browser  > backend service > backend processing > browser

curl 'https://api.bank.easyitlab.tech/students/employees' \
  -H 'accept: */*' \
  -H 'accept-language: ru,en-GB;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxYjFkZjBjYy1mMjIzLTRlZDMtODA4MS0yMjE1NTM2ZjhkZmMiLCJ1c2VyX2lkIjoiMWIxZGYwY2MtZjIyMy00ZWQzLTgwODEtMjIxNTUzNmY4ZGZjIiwic3lzdGVtX3JvbGUiOiJTVFVERU5UIiwiYnVzaW5lc3Nfcm9sZSI6IkNMSUVOVCIsInBlcm1pc3Npb25zIjpbImNsaWVudDphY2NvdW50czpyZWFkIiwiY2xpZW50OnRyYW5zZmVyczpjcmVhdGUiLCJjbGllbnQ6dGlja2V0czpjcmVhdGUiXSwic2Vzc2lvbl9pZCI6ImY2NjE5ZTI2YTg2ZTQ4ZmY4NzczMzdhM2Q4ZjY3MGI1IiwiaWF0IjoxNzc1MTQ3MzQ1LCJleHAiOjE3NzUxNDgyNDUsInR5cGUiOiJhY2Nlc3MifQ.aGsUd-djMojKsSR1x7tvSzJ8sA0CgWAh3q1uyTZoGK8' \
  -H 'content-type: application/json' \
  -H 'origin: https://student.bank.easyitlab.tech' \
  -H 'priority: u=1, i' \
  -H 'referer: https://student.bank.easyitlab.tech/' \
  -H 'sec-ch-ua: "Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
"""


"""
GET
POST
PUT
PATCH
DELETE
"""

"""
1**
100
101

2**
200
201
204

3**

4**
400 
401
403
404

5**
500
502
504
"""

import requests
from faker import Faker
from requests import Response

fake = Faker()



BASE_URL = 'https://api.bank.easyitlab.tech'

EMAIL = "gravitel0nd@gmail.com"
PASSWORD = "XH0RvnaAhSZt"

login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={"email": EMAIL, "password": PASSWORD},
    timeout=15,
)
login_response.raise_for_status()
tokens = login_response.json()
TOKEN = tokens["access_token"]


HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

def create_employee():
    body = {
        "email": fake.ascii_company_email(),
        "full_name": "Daniil Nikolaev"
    }
    created_employee = requests.post(
        url=f"{BASE_URL}/students/employees",
        headers=HEADERS,
        json=body
    )
    assert created_employee.status_code == 200
    employee_id = created_employee.json().get('id')
    return employee_id

def delete_employee(employee_id):
    requests.delete(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers={
            'Authorization': f'Bearer {TOKEN}'
        }
    )

def get_id(get_employee: Response):
    get_employee_json = get_employee.json()
    employee_id = get_employee_json.get('id')
    assert employee_id is not None
    return employee_id


def test_employee():
    employee_id = create_employee()

    get_employee = requests.get(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers=HEADERS

    )
    assert get_employee.status_code == 200
    assert get_id(get_employee) == employee_id

    name = fake.name()

    body = {
        "email": fake.ascii_company_email(),
        "full_name": name
    }

    patch_employee = requests.patch(
        f"{BASE_URL}/students/employees/{employee_id}",
        json= body,
        headers=HEADERS
    )
    assert get_employee.status_code == 200

    get_employee = requests.get(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers=HEADERS
    )
    assert get_employee.status_code == 200
    get_employee_json = get_employee.json()

    assert get_employee_json['full_name'] == name

    delete_employee(employee_id)