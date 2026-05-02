import unittest
import requests


BASE_URL = 'https://api.bank.easyitlab.tech'

def get_token():
    token_response = requests.post(
        f"{BASE_URL}/auth/login",
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

    token = token_response_json.get('access_token')
    assert token, "token not found"
    return token

def get_auth_headers():
    headers = {
        "Authorization": f"Bearer {get_token()}",
        'Content-Type': 'application/json'
    }
    return headers


class TestStudentDashboard(unittest.TestCase):

    def ttest_get_dashboard_success(self):
        headers = get_auth_headers()

        students_dashboard = requests.get(
            f"{BASE_URL}/students/dashboard",
            headers=headers
        )

        self.assertEqual(students_dashboard.status_code, 200)

        students_dashboard_json = students_dashboard.json()

        self.assertIn('employees_total', students_dashboard_json)
        self.assertIn('clients_total', students_dashboard_json)
        self.assertIn('accounts_total', students_dashboard_json)
        self.assertIn('tickets_total', students_dashboard_json)


if __name__ == '__main__':
    unittest.main()
else:
    print("__name__", __name__)


