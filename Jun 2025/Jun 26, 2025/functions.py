from typing import Tuple, Any, Union

# How can we write the type hints if we are returning multiple values?

# def get_input():
#     input1 = 12
#     input2 = "Ronald Johnson"
#     input3 = "USA"
#     return input1, input2, input3


# 1) Tuple

# def get_input() -> tuple[int, str, str]:
#     input1 = 12
#     input2 = "Ronald Johnson"
#     input3 = "USA"
#     return input1, input2, input3


# 2) class
# 3) dict

# def get_input() -> dict:
#     input1 = 12
#     input2 = "Ronald Johnson"
#     input3 = "USA"
#     inputs = {
#         "Roll Number": input1,
#         "Name": input2,
#         "Address": input3
#     }
#     return inputs


# 4) list

def get_input() -> list[str]:
    input1 = 12
    input2 = "Ronald Johnson"
    input3 = "USA"
    return [input1, input2, input3]


# Type Hints
# ( Multiple values )

# Union


def return_one_value(num) -> Union[int, str]:
    if num == 1:
        return str(num * 100)
    return num * 100


def return_values(num) -> Tuple[Union[str, int], Union[int, str]]:
    if num == 1:
        return str(num * 100), num + 100
    return num * 100, str(num + 100)

# Any

def return_value(num) -> Tuple[Any, ...]:
    if num == 1:
        return str(num * 100), 100
    elif num == 2:
        return True, 100
    return num * 100, 100


# *arg

def find_sum(num1, num2):
    return num1 + num2

def find_sum_three(num1, num2, num3):
    return num1 + num2 + num3


def find_numbers_sum(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

print(find_numbers_sum(1, 4, 5, 67, 54))


def get_inputs():
    input1 = 12
    input2 = "Ronald Johnson"
    input3 = "USA"
    return input1, input2, input3

# 1) Collection
var1 = get_inputs()
print(type(var1))

# 2) Multiple Assignment
# var1, var2, var3 = get_inputs()

# var1, var2 = get_inputs()

# 3) Unpacking the returned values from the function

var1, *var2 = get_inputs()



# **karg
# scope of variables
# nested functions
# lambda
# recursion
# high order functions
# @decorator
# pass by value vs pass by reference
# shallow copy vs deep copy