# import os
#
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.timedelta(days=10, hours=10))

# import random

# from random import random as r, randint, randrange, choice
#
#
# print(r())
# print(randint(1, 10))
# print(randrange(10, 100, 5))
# print(choice([10, 11, 12]))

# from random import *

# import os
# from random import choice
# import datetime
#
# users = ["ivan@example.com", "daniil@example.com", "igor@example.com", "john@example.com"]
#
# user = choice(users)
#
# today = datetime.datetime.now()
#
# base_path = os.path.dirname(__file__)
#
# print(user)
# print(today)
# print(base_path)

# file = open('11_emails.txt', 'r')
# emails = file.read()
# print(emails)
# file.close()

# with open('11_emails.txt', 'r') as f:
#     emails = f.read()
#
# print(emails)

# class OpenFile:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, *args):
#         if self.file:
#             self.file.close()
#
# with OpenFile('11_emails.txt', 'a') as f:
#     f.write('\nanna@example.com')

import os
#
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '11_app.log')
#
# with open(file_path, 'r') as f:
#     logs = f.read()
#
# assert 'ERROR' not in logs, (
#     "Errors in log\n",
#     f'LOGS:\n{logs}'
# )

# with open(file_path, 'r') as f:
#     logs = f.readlines()

# print(logs)
#
# for log in logs
# iter_logs = iter(logs)
# print(next(iter_logs))
# print(next(iter_logs))
# print(next(iter_logs))
#
# def read_file():
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             yield line
#
# for l in read_file():
#     assert 'ERROR' not in l, (
#         "Errors in log\n",
#         f'Line:\n{l}'
#     )
# a = [10, 11, 12]
# for i in range(len(a)):
#     print(i)

# """
# map(function, collection)
# """
# str(1)
# numbers = ["1", "2", "3"]
# result = map(int, numbers)
#
# print(tuple(result))

# with open("11_users_ids.txt", 'r') as f:
#     user_ids = f.readlines()
#
# user_ids = list(map(int, user_ids))
#
# print(user_ids)

# with open("11_prices.txt", 'r') as f:
#     prices = f.readlines()
#
# prices = list(map(int, prices))
# new_prices = list(map(lambda price: int(price * 1.1), prices))
#
# with open("11_new_prices.txt", 'w') as f:
#     for new_price in new_prices:
#         f.write(str(new_price) + '\n')
#
# print(new_prices)

# emails = ["ivan@example.com", "daniil@example.com", "igor@example.com", "john@example.com", "john@example.com", "john@example.com", "john@example.com", "john@example.com", "john@example.com"]
# access = [True, False, True, True]
#
# result = dict(zip(emails, access))
# print(result)
#
# numbers = ["1", "2", "3"]
# result = list(map(int, numbers))
#
# result_2 = [int(number) for number in numbers]

# #
import datetime
# #
# # now = datetime.datetime.now()
# # print(datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
# # print(now - datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
#
# created_at = datetime.datetime.now()
# expires_at = created_at + datetime.timedelta(minutes=7)
#
# print(datetime.timedelta(minutes=7))
# print(created_at)
# print(expires_at)

# try:
#     file = open("11_new_prices.txt", "r")
#     data = file.read()
# except FileNotFoundError as err:
#     with open(file_path, 'a') as f:
#         f.write(f"\n{datetime.datetime.now().replace(microsecond=0)} ERROR Read error: {err}")
#     print(f"Read error: {err}")
# else:
#     print("File read success")
# finally:
#     file.close()

response = {'status1': "ERROR"}

def parse_status(resp):
    try:
        status = int(response['status'])
    except (KeyError, ValueError) as err:
        print(f'Error response: {response}')
        raise err
    else:
        return status
    finally:
        print('Parsing finish')

status = parse_status(response)

print(status)

