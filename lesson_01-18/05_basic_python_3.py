# numbers = [1, 2, 3]
# print(numbers)

# data = [1, "hello", 1.23, False]
# print(data)
# print(type(data))
#
# print(data[2])
# print(type(data[2]))
# print(data[-1])

# data[0] = 100
# data[1] = True
# print(data)
#
# print(data[1][-1])
# numbers = [1, 2, 3]
# print(numbers)
# numbers.append(5)
# numbers.append(3)
# print(numbers)
# numbers.extend([4, 5])
# print(numbers)
# numbers.remove("hello")
# print(numbers)
# numbers.insert(3, 456)
# print(numbers)
# el = numbers.pop()
# print(el)
# numbers.pop()
# numbers.pop()
# numbers.pop()
# print(numbers)

# numbers = [1, 2, 3]

# for num in numbers:
#     print(num)

# data = [1, "hello", 1.23, False]
# for index, value in enumerate(data):
#     print('index:', index, 'value:', value)
# sq = []
# sq = list()
# for x in range(1, 6, 2):
#     sq.append(x * x)
# sq = [x * x for x in range(1, 6, 2)]
# print(sq)

# ages = (4, 20, 35, 18)
# print(ages)
# print(id(ages))
# print(ages[1])

# ages_1 = (4, 20, 35, 18) + (90,)
# print(ages_1)
# print(id(ages_1))

# user = {
#     'name': "Daniil",
#     "surname": "Nikolaev"
# }
# print(user)
# print(user["surname"])
# print(user.get("name", "Attribute not found"))

# user['age'] = 36
# user['name'] = "Danya"
# print(user)

# for key in user:
#     print(key)

# for value in user.values():
#     print(value)

# for key, value in user.items():
#     print(key, value)

# response = {
#     'status': 'COMPLETED',
#     'additionInfo': {
#         'statuses': ['COMPLETED', 'ERROR', 'PROCESSING'],
#         'id': "eewq32-d23f32d-f32f32-f32f32-fvvng"
#     },
#     'structure': 'DONE'
# }
# print(response['status'])
# print(response['additionInfo']['statuses'])
# print(response['additionInfo']['statuses'][2])

# response = {
#     'objects': [
#         {
#             'status': 'COMPLETED',
#             'additionInfo': {
#                 'statuses': ['COMPLETED', 'ERROR', 'PROCESSING'],
#                 'id': "eewq32-d23f32d-f32f32-f32f32-fvvng"
#             },
#             'structure': 'DONE'
#         },
#         {
#             'status': 'ERROR',
#             'additionInfo': {
#                 'statuses': ['COMPLETED', 'ERROR', 'PROCESSING'],
#                 'id': "fwefwef-fwef-fnhgn -f3hjhj2-32534tr"
#             },
#             'structure': 'DONE'
#         },
#         {
#             'status': 'ERROR',
#             'additionInfo': {
#                 'statuses': ['COMPLETED', 'ERROR', 'PROCESSING'],
#                 'id': "ageer-fwef-fnhgn -f3hjhj2-32534tr"
#             },
#             'structure': 'DONE'
#         }
#     ]
#
# }
#
# ids_error = []
#
# for obj in response['objects']:
#     if obj['status'] == 'ERROR':
#         ids_error.append(obj['additionInfo']['id'])
#
# print(ids_error)

# d = dict()

# s = {1, 2, 4, 4}
# l = [1, 2, 3, 4, 4, 4]
# s = set(l)
# print(s)

