

# Functions

# type of functions -> built in, user defined

# 1) Build it functions     -> count, count, len, print
# 2) User defined functions  -> custom functions


# def

def print_something():
    print("something")


# function parts

# 1) Function headers
    # - def
    # - function name
    # - parameters (Optional)
    # - ():
    # - type hints (Optional)

# 2) Function Body
    # - block of code (at least one line of code)
    # - return


# return

# n(n+1)/2

def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(90, 76))

result1 = sum_numbers(50, 0)
result2 = sum_numbers(90, 87)
result = result1 + result2

print(result)

# arg

# - The data we are passing to the function through the function call.

# parameters

# - The data which we are accepting in the function header.


# Positional arguments
print(sum_numbers(87, 90))


# key arguments

def print_user(first_name, last_name, address):
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Address: {address}")

# print_user("Ronald", "Johnson")
# print_user("Johnson", "Ronald")

print_user("Johnson", "Ronald", address="House No: 19, USA.")


# default parameters

def print_user1(first_name, last_name="Johnson", address="House No: 19, USA."):
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Address: {address}")

print_user1("Johnson")



# function annotations -> type hints
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