# age = 17
#
# if age >= 18: # False
#     print("Access")

# age = 16
#
# if age >= 18: # True
#     print("Access")
# else:
#     print('Deny')

#
# count = 4
#
# if count >= 10:
#     print("discount 20%")
# elif count >= 5:
#     print("discount 10%")
# else:
#     print('discount 0%')

# count = 5
# sum_basket = 10000
# if count >= 5 and sum_basket >= 10000:
#     print("discount 20%")


# count = 4
# sum_basket = 10000
# if (count >= 5) or (sum_basket >= 10000) and ((count * sum_basket) < 100000):
#     print("discount 20%")

# is_user = False
#
# if not is_user:
#     print("discount 20%")

# count = 4
#
# if count >= 5:
#     if count >= 10:
#         print("discount 20%")
#     else:
#         print("discount 10%")
# else:
#     print('discount 0%')

# attrs = [1, "hello", 1.23, False]
#
# for attr in attrs:
#     print(attr)
#     attrs.remove(attr)
#
# print(attrs)
#
# for i in range(len(attrs)):
#     print(attrs[i])


# attrs = [1, "hello", 1.23, False]

# i = 1
#
# while i < 11:
#     print(i)
#     i += 1

# attrs = [1, "hello", 1.23, False]
# for attr in attrs:
#     print(attr)

# status = "Success"
# status_error = "Error"
#
# status_input = input("Status from service: ")
# while status != status_input:
#     if status_input == status_error:
#         break
#     status_input = input("Status from service: ")
#
# print("Status:", status_input)


# attrs = [1, "hello", 1.23, False]
# for attr in attrs:
#     if isinstance(attr, (int, float)) and not isinstance(attr, bool):
#         continue
#     print(attr)

# while True:
#     print(123)

response = {
    'user': "Daniil",
    'is_admin': False,
}

if response['is_admin']:
    interface = "create"
else:
    interface = "view"

# interface = "create" if response['is_admin'] else 'view'
print(interface)