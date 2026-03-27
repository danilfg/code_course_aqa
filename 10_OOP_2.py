# class User:
#     def __init__(self, email, age, token):
#         self.email = email
#         self._age = age
#         self.__token = token
#
#
# user = User('adffw@asfa.ru', 17, 'egewfwegwegewfcEWFEWFEW3252')
# print(user.email)
# print(user._age)
# print(user.__token)

# class ApiClient:
#     def __init__(self, token):
#         self.__token = token
#
#     def get_headers(self):
#         return {"Authorization": f"Bearer {self.__token}"}
#
# client = ApiClient('sfwefew')
# print(client.get_headers())
#
# class User:
#     def __init__(self, age):
#         self._age = age
#
#     def get_age(self):
#         return self._age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age must be positive")
#         self._age = value
#
# user = User(25)
# print(user.age)
# user.age = 20
# print(user.age)

# class ResponseWrapper:
#     def __init__(self, status_code):
#         self._status_code = status_code
#
#     @property
#     def status_code(self):
#         return self._status_code
#
#     @property
#     def is_success(self):
#         return 200 <= self._status_code < 300
#
#
# response = ResponseWrapper(404)
# print(response.status_code)
# print(response.is_success)

# class UserApi:
#     def get_users(self):
#         print('Real users')
#
# class MockUserApi:
#     def get_users(self):
#         print('Mock users')
#
# def run_test(api):
#     api.get_users()
#
# run_test(UserApi())
# run_test(MockUserApi())

# class AuthService:
#     def get_token(self):
#         return 'token'
#
# class ApiClient:
#     BASE_URL = "http://google.com"
#
#     def __init__(self):
#         self.auth_service = AuthService()
#
#     @classmethod
#     def get_url(cls):
#         return cls.BASE_URL
#
#     @staticmethod
#     def check_token(token):
#         if token != 0:
#             return token
#         else:
#             raise ValueError('Token not work')
#
#     @property
#     def token(self):
#         token = self.check_token(self.auth_service.get_token())
#         return token
#
#     def get_headers(self):
#         return {"Authorization": f"Bearer {self.token}"}
#
# client = ApiClient()
# print(client.get_headers())
#
# print(client.__dict__)
# print(ApiClient.get_url())

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"User(name={self.name})"
#
#     def __repr__(self):
#         return f"User('{self.name}')"
#
# user = User("Daniil")
# print(user)
# print([user])

from abc import abstractmethod
from abc import ABC

class Person(ABC):
    def __init__(self, login):
        self.login = login

    @abstractmethod
    def get_name(self):
        return self.login

class Admin(Person):
    def __init__(self, login):
        super().__init__(login)

    def get_name(self):
        return self.login

class User(Person):
    def __init__(self, login):
        super().__init__(login)

    def get_name(self):
        return self.login


admin = Admin('Daniil')