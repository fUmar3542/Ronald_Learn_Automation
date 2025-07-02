
# *arg

# def find_numbers_sum(*numbers):
#     sum = 0
#     for x in numbers:
#         sum += x
#     return sum
#
# print(find_numbers_sum(1, 4, 5, 67, 54))


# def print_user(*arg):
#     for x in arg:
#         print(x)
#
#
# print_user(12, "Ronald Johnson", "USA", "+1871379379193")


# def print_user_position(roll, name, country):
#     print(roll)
#     print(name)
#     print(country)
#
# print_user_position(name="Ronald Johnson", country="USA", roll=12)


# **karg


# def print_user(**data):
#     for x in data:
#         print(f"{x}: {data[x]}")

# def print_user(**data):
#     for x, y in data.items():
#         if x == "subjects":
#             print(x)
#             for value in data[x]:
#                 print(value)
#         else:
#             print(f"{x}: {y}")

# def print_user(**data):
#     for x, y in data.items():
#         if type(x) == list:
#             print(x)
#             for value in data[x]:
#                 print(value)
#         else:
#             print(f"{x}: {y}")


def print_user(*arg, **data):
    for x, y in data.items():
        print(f"{x}: {y}")
    print("Subjects: ")
    for x in arg:
        print(x)

print_user(roll_number=12, name="Ronald Johnson", country="USA", phone_number="+1871379379193")
print("------------------------------------")
print_user(roll_number=12, name="Ronald Johnson", country="USA", subjects=["Science", "Math"])
print("------------------------------------")
print_user("Science", "Math", roll_number=12, name="Ronald Johnson", country="USA")



# scope of variables
# nested functions
# lambda
# recursion
# high order functions
# @decorator
# pass by value vs pass by reference
# shallow copy vs deep copy