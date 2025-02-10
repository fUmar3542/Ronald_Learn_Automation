

################################################################################################################

# Arguments vs parameters

# Arguments
# The values which we are passing to the function.

# Parameters
# The values which the function is accepting to perform the specific operation.

# # Parameters -> value
# def print_hello(value):
#     print(value)
#
#
# # Argument -> "Hello"
# print_hello("Hello")


################################################################################################################

# Types of function according to their specifications

# 1) Function without parameters / Default function
# Function without any parameters.

# def print_hello():
#     print("Hello")
#
# # print_hello()


# 2) Parametrized functions

# Return statement
# Returning from the function with or without the values to the line where the function was called.

# If the return statement is without any values and it is written as the last line of the function,
# there is no need to write the return statement there

# 1. First implementation
def print_hello(value1, value2):
    print(value1, value2)


# 2. Second implementation
# Parameters -> value
def print_hello(value1, value2):
    if value1 == "Hello":
        print(value1)
    else:
        print(value1, value2)
    print()
    print()


# Argument -> "Hello"
print_hello("Hello", "World")
print_hello("World", "Hello")


# Create a parametrized function which is accepting two integers and it is


def do_something():
    print()
    print()
    print()


print()
print()
print()
do_something()
print()
print()
print()

# User choice function
# if 1:
# create
# elif 2:
# Update
