import pytest
import requests
import allure

from unittest.mock import Mock


@allure.feature("Dashboard")
@allure.story("Get dashboard")
@allure.title("Get dashboard")
@allure.description("Check dashboard")
def test_get_dashboard_success(base_url, auth_headers):

    with allure.step("Send GET /students/dashboard"):
        students_dashboard = requests.get(
                f"{base_url}/students/dashboard",
                headers=auth_headers
            )
    with allure.step(f"Check status code 200"):
        assert students_dashboard.status_code == 200

    with allure.step(f"Check response body"):
        students_dashboard_json = students_dashboard.json()

        assert "employees_total" in students_dashboard_json
        assert "clients_total" in students_dashboard_json
        assert "accounts_total" in students_dashboard_json
        assert "tickets_total" in students_dashboard_json


class FakeDashboardResponse:
    status_code = 200

    def json(self):
        return {'accounts_total': 0,
                 'clients_total': 0,
                 'employees_active': 13,
                 'employees_blocked': 0,
                 'employees_total': 13,
                 'series': [{'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-06',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-07',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-08',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-09',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-10',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-11',
                             'employees': 0,
                             'tickets': 0},
                            {'accounts': 0,
                             'clients': 0,
                             'day': '2026-05-12',
                             'employees': 0,
                             'tickets': 0}],
                 'tickets_total': 0,
                 'transfers_total': 0}


@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Get dashboard with stub")
@allure.description("Check dashboard from stub")
def test_get_dashboard_with_stub(monkeypatch, base_url, auth_headers):
    def fake_get(url, headers):
        return FakeDashboardResponse()

    monkeypatch.setattr(requests, 'get', fake_get)

    with allure.step("Send GET /students/dashboard"):
        students_dashboard = requests.get(
                f"{base_url}/students/dashboard",
                headers=auth_headers
            )

    with allure.step(f"Check status code 200"):
        assert students_dashboard.status_code == 200

    with allure.step(f"Check response body"):
        students_dashboard_json = students_dashboard.json()

        assert "employees_total" in students_dashboard_json
        assert "clients_total" in students_dashboard_json
        assert "accounts_total" in students_dashboard_json
        assert "tickets_total" in students_dashboard_json


@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Get dashboard with Mock")
@allure.description("Check dashboard from Mock")
def test_get_dashboard_with_mock(monkeypatch, base_url, auth_headers):
    fake_response = Mock()

    fake_response.status_code = 200
    fake_response.json.return_value = {'accounts_total': 0,
                                         'clients_total': 0,
                                         'employees_active': 13,
                                         'employees_blocked': 0,
                                         'employees_total': 13,
                                         'tickets_total': 0,
                                         'transfers_total': 0}

    requests_get_mock = Mock(return_value=fake_response)

    monkeypatch.setattr(requests, 'get', requests_get_mock)

    with allure.step("Send GET /students/dashboard"):
        students_dashboard = requests.get(
                f"{base_url}/students/dashboard",
                headers=auth_headers
            )

    with allure.step(f"Check status code 200"):
        assert students_dashboard.status_code == 200

    with allure.step(f"Check response body"):
        students_dashboard_json = students_dashboard.json()

        assert "employees_total" in students_dashboard_json
        assert "clients_total" in students_dashboard_json
        assert "accounts_total" in students_dashboard_json
        assert "tickets_total" in students_dashboard_json

    with allure.step(
            'Check requests.get was called with correct url and headers'
    ):
        requests_get_mock.assert_called_once_with(
            f"{base_url}/students/dashboard",
            headers=auth_headers
        )

    with allure.step("Check json method was called"):
        fake_response.json.assert_called_once()


@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Dashboard requests failed")
def test_get_dashboard_requests_failed(
    monkeypatch, base_url, auth_headers
):
    requests_get_mock = Mock(
        side_effect=requests.ConnectionError("Service unavailable")
    )

    monkeypatch.setattr(requests, 'get', requests_get_mock)

    with pytest.raises(requests.ConnectionError):
        requests.get(
            f"{base_url}/students/dashboard",
            headers=auth_headers
        )

    requests_get_mock.assert_called_once_with(
        f"{base_url}/students/dashboard",
        headers=auth_headers
    )