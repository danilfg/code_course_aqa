users = {
    "users": [
        {
            'name': 'Daniil',
            'age': 19,
            'id': 1
        },
        {
            'name': 'Igor',
            'age': 14,
            'id': 2
        },
        {
            'name': 'Ivan',
            'age': 18,
            'id': 3
        }
    ]
}

# names = []
# for user in users['users']:
#     names.append(user['name'])
# names = [user['name'] for user in users['users']]
#
# names = [user['name'] for user in users['users'] if user['age'] >= 18]
# print(names)

# orders = {
#     'orders': [
#         {
#             'id': 1,
#             'status': 'paid'
#         },
#         {
#             'id': 2,
#             'status': 'paid'
#         },
#         {
#             'id': 3,
#             'status': 'cancelled'
#         }
#     ]
# }
#
# paid_orders = [order['id'] for order in orders['orders'] if order['status'] == 'paid']
# print(paid_orders)
#
# cancelled_orders = [order['id'] for order in orders['orders'] if order['status'] == 'cancelled']
# print(cancelled_orders)
#

# def logger(func):
#     def wrapper():
#         print('Start func')
#         func()
#         print("End func")
#     return wrapper
#
# @logger
# def get_id_users():
#     print(123)
#
# get_id_users()
# print(id(get_id_users))
# print(get_id_users())

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print('func:', func)
#         print('Start func')
#         result = func(*args, **kwargs)
#         print("End func")
#         return result
#     return wrapper
#
# @logger
# def get_id_users(name, email):
#     for user in users['users']:
#         if user['name'] == name:
#             print("user['name']:", user['name'])
#             return user['id']
#
# name = "Daniil"
# email_user = 'asda@ADS.ey'
# print(get_id_users(name, email=email_user))

@logger
@check
def id_name(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

id_name(123, ('asa', True), 'Daniil', age=36)



[num for num in numbers if num > 35 or num == 0]

