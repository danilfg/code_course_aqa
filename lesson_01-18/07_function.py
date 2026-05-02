# def say_hello():
#     print("hello")
#
# say_hello()



# def create_user():
#     print("Create user")
#     print("Send request")
#     print("Check status")
#
# create_user()
# create_user()
# create_user()
# create_user()

# def create_user(name, email):
#     print(f"Create user: {name}, {email}")
#
# print(create_user("Daniil", "admin@vk.ru"))
#
#
# # create_user("Daniil", "admin@vk.ru")
#
#
# name_user = "Daniil"
# email_user = "admin@vk.ru"
#
# create_user(name_user, email_user)

# users = {
#     "users": [
#         {
#             'name': 'Daniil',
#             'id': 1
#         },
#         {
#             'name': 'Igor',
#             'id': 2
#         }
#     ]
# }

# def get_id_user(name):
#     users_list = users["users"]
#     for user in users_list:
#         if user['name'] == name:
#             return user['id']
#
#     return "Name not found"
#
# id_user = get_id_user('dsfsr')
# print(id_user)

# users = {
#     "users": [
#         {
#             'name': 'Daniil',
#             'age': 19,
#             'id': 1
#         },
#         {
#             'name': 'Igor',
#             'age': 14,
#             'id': 2
#         },
#         {
#             'name': 'Ivan',
#             'age': 18,
#             'id': 3
#         }
#     ]
# }
#
# def has_adult(age):
#     users_list = users['users']
#     ids_adult = []
#     for user in users_list:
#         if user['age'] >= age:
#             ids_adult.append(user['id'])
#     return ids_adult
#
# ids_list = has_adult(19)
#
# print(ids_list)


# def retry_request(count):
#     attepts = count
#     while attepts > 0:
#         print("Send request")
#         attepts -= 1
#
# retry_request(3)

# def create_user():
#     user_id = 100
#     return user_id
#
# user_id = create_user()
# print(user_id)


def retry_request(count=3):
    attepts = count
    while attepts > 0:
        print("Send request")
        attepts -= 1

retry_request(5)