import json
from pprint import pprint
from unittest.mock import Mock

import allure
import requests

from faker import Faker

from helpers.allure_helper import attach_json

fake = Faker()


@allure.feature("Employee")
@allure.story("Get employees")
@allure.title("Get employees")
@allure.suite('Employee API')
@allure.description("Check list of employees")
def test_get_employees_success(base_url, auth_headers):
    with allure.step("Send GET /students/employees/"):
        employees = requests.get(
            f"{base_url}/students/employees",
            headers=auth_headers
        )
    with allure.step(f"Check status code 200"):
        assert employees.status_code == 200, (
            'Expected: 200\n'
            f'Actual: {employees.status_code}'
        )

    with allure.step(f"Get json response"):
        employees_json = employees.json()
    with allure.step(f"Check body answer is list"):
        assert isinstance(employees_json, list)

@allure.feature("Employee")
@allure.story("Created employee")
@allure.title("Created employee")
@allure.suite('Employee API')
@allure.description("Check created employee")
def test_created_employee(base_url, auth_headers):
    with allure.step("Prepare payload"):
        email = fake.email()
        full_name = fake.name()

        payload = {
            'email': email,
            'full_name': full_name
        }

    attach_json(json.dumps(payload), "Payload")

    with allure.step("Send POST /students/employees/"):
        created_employee = requests.post(
            f"{base_url}/students/employees",
            headers=auth_headers,
            json=payload
        )

    with allure.step(f"Check status code 200"):
        assert created_employee.status_code == 200

    with allure.step(f"Get json response"):
        created_employee_json = created_employee.json()

    with allure.step(f"Check email employee"):
        assert created_employee_json['email'] == email

    with allure.step(f"Check full_name employee"):
        assert created_employee_json['full_name'] == full_name

    with allure.step(f"Delete /students/employees/{created_employee_json['id']}"):
        requests.delete(
            f"{base_url}/students/employees/{created_employee_json['id']}",
            headers=auth_headers
        )


@allure.feature("Employee")
@allure.story("Get employee")
@allure.title("Get employee")
@allure.suite('Employee API')
@allure.description("Check created employee")
def test_get_employee(base_url, auth_headers, created_employee):
    id_employee, email, full_name = created_employee
    with allure.step(f"Send GET /students/employees/{id_employee}"):
        employee = requests.get(
            f"{base_url}/students/employees/{id_employee}",
            headers=auth_headers
        )

    attach_json(employee.text, "Response body")

    with allure.step(f"Check status code 200"):
        assert employee.status_code == 200

    with allure.step(f"Get json response"):
        employee_json = employee.json()

    with allure.step(f"Check email employee"):
        assert employee_json['email'] == email

    with allure.step(f"Check full_name employee"):
        assert employee_json['full_name'] == full_name


@allure.feature("Employee")
@allure.story("Mock and monkeypatch")
@allure.title("Get employee with mock")
def test_create_employee_with_mock(monkeypatch, base_url, auth_headers):
    with allure.step("Prepare payload"):
        email = fake.email()
        full_name = fake.name()

        payload = {
            'email': email,
            'full_name': full_name
        }

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {'clients_count': 0,
                                         'created_at': '2026-05-12T16:10:38.320480Z',
                                         'email': email,
                                         'first_name': 'Gerald',
                                         'full_name': full_name,
                                         'id': 'st-0352',
                                         'is_active': True,
                                         'is_blocked': False,
                                         'last_login_at': None,
                                         'last_name': 'Miller',
                                         'status': 'ACTIVE',
                                         'tickets_count': 0,
                                         'updated_at': '2026-05-12T16:10:38.320480Z',
                                         'username': 'ebanks@example.org',
                                         'uuid': '9db74fdb-230d-40a1-bb5c-c1ac58d7a89d'}

    requests_post_mock = Mock(return_value=fake_response)
    monkeypatch.setattr(requests, 'post', requests_post_mock)

    with allure.step("Send POST /students/employees/"):
        created_employee = requests.post(
            f"{base_url}/students/employees",
            headers=auth_headers,
            json=payload
        )

    with allure.step(f"Check status code 200"):
        assert created_employee.status_code == 200

    with allure.step(f"Get json response"):
        created_employee_json = created_employee.json()

    with allure.step(f"Check email employee"):
        assert created_employee_json['email'] == email

    with allure.step(f"Check full_name employee"):
        assert created_employee_json['full_name'] == full_name

    with allure.step('Check requests.post was called with correct payload'):
        requests_post_mock.assert_called_once_with(
            f"{base_url}/students/employees",
            headers=auth_headers,
            json=payload
        )

    with allure.step("Check json method was called"):
        fake_response.json.assert_called_once()