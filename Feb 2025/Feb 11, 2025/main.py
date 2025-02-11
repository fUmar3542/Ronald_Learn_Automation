

#########################################################################################

# Parametrized function

# 1) Function with one parameter
# 2) Function with multiple parameters

def print_hello(value1, value2):
    if value1 == "Hello":
        print(value1)
    else:
        print(value1, value2)
    print()
    print()


# Argument -> "Hello"
# print_hello("Hello", "World")
# print_hello("World", "Hello")


# 3) Function with key arguments

#
# print_hello("Hello", "World")
#
# # Without the order of parameters
# print_hello(value1="Hello", value2="World")
# print_hello(value2="Hello", value1="World")


# 3) Function with default parameters


# def sum_numbers(value1=8, value2=9):
#     print(value1 + value2)

# ------------------------------------------------------------------------------

# Write a program to print the sum of two numbers.
# To find and print the sum, use the function sum_numbers().

# def sum_numbers(value1, value2):
#     print(value1 + value2)
#
#
# sum_numbers(10, 5)


# def sum_numbers1(value1):
#     print(value1 + 5)


# sum_numbers(10)

count = 9

#
# def sum_numbers(value1=8, value2=count):
#     print(value1 + value2)
#
#
# sum_numbers()
#
#
# name = "Ronald"
# name1 = name

# ------------------------------------------------------------------------------

# 5) Function with return statement


# def hello_print():
#     print()
#     print()
#     return
#
#
# print()
# hello_print()
# print()

def hello_print():
    print(1)
    print(2)
    return 9


print("-")
result = hello_print()
print(result)
print("-")


user_input = input("Enter a number: ")

