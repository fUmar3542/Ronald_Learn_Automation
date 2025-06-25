

# function annotations -> type hints

# Data types written with the function parameters just for clarity

# def print_user(roll_number, name, address):
#     print(f"Roll Number: {roll_number}")
#     print(f"Name: {name}")
#     print(f"Address: {address}")


def print_user(roll_number : int, name : str, address : str):
    print(f"Roll Number: {roll_number}")
    print(f"Name: {name}")
    print(f"Address: {address}")


print_user(1, "Ronald Johnson", "California, USA")


def find_sum(num1 : int, num2 : int) -> int:
    return num1 + num2


print(find_sum(23, 45))


# How can we write the type hints if we are returning multiple values?



# *arg
# **karg
# scope of variables
# nested functions
# lambda
# recursion
# high order functions
# @decorator
# pass by value vs pass by reference
# shallow copy vs deep copy