# class User:
#     pass
#
# user = User()


# class User:
#     def __init__(self, email, password):
#         # print('self: ', id(self))
#         self.email = email
#         self.password = password
#
#     def login(self):
#         print("Login with ", self.email)
#
#
# user = User("test@test.ru", 'pass')
# # print('user: ', id(user))
# # print('User: ', id(User))
# #
# # print(type(user))
# user.login()
#
# lst = [1,2,3]
# lst.append(4)
#
# class ApiClass:
#     base_url = "https://api.test.com"
#
# client = ApiClass()
#
# print(client.base_url)

#
# class User:
#     role = 'user'
#
# u1 = User()
# u2 = User()
#
# # print(u1.role)
# # print(u2.role)
# #
# # print(id(u1.role))
# # print(id(u2.role))
# print(User.__dict__)
#
#
# print(u1.__dict__)
# print(u2.__dict__)
#
# u1.role = 'admin'
#
# # print(u1.role)
# # print(u2.role)
# #
# # print(id(u1.role))
# # print(id(u2.role))
#
# print(u1.__dict__)
# print(u2.__dict__)

# class A:
#     x = 10
#
# a = A()
# b = A()
#
# a.x = 20
#
# print(a.x, b.x)

# class User:
#     def __init__(self, email):
#         self.email = email
#
# user = User('test@test.ru')
# print(id(user))
#
# user.email = 'admin@admin.ru'
#
# print(id(user))

# class User:
#     pass
#
# user = User()
#
# print(user.__dict__)
#
# user.email = 'admin@admin.ru'
#
# print(user.__dict__)
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
# cart1 = Cart()
# cart2 = Cart()
#
# cart1.items.append("Laptop")
#
# print(cart1.items)
# print(cart2.items)

#
# class API:
#     def request(self, method, url):
#         print("API: ", method, url)
#
# class BaseAPI(API):
#     def request(self, method, url):
#         print("BaseAPI: ", method, url)
#
# class UserAPI(BaseAPI):
#     # def request(self, method, url):
#     #     print("UserAPI:", method, url)
#
#     def get_users(self):
#         self.request("GET", "/users")
#
# api = UserAPI()
# api.get_users()
#
# print(UserAPI.__mro__)


# class BaseAPI:
#
#     def request(self):
#         print("BaseAPI")
#
# class UserAPI(BaseAPI):
#
#     def request(self):
#         super().request()
#         print("UserAPI")
#
# api = UserAPI()
#
# api.request()

class User:

    def __init__(self):
        pass

user = User()