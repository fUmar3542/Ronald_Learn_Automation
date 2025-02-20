username = "175qwdjw"   # Global variable

# Nested Functions

###########################################################################################################################

# First example

# def print_something():
#     print()
#
#
# def print_dict(**info):
#     # global username
#     username = "jwegfu828"
#     print(username)
#     count = 0
#
#     def display_key_values():
#         for key, value in info.items():
#             print(f"{key}: {value}")
#
#     def display_marks():
#         for i in info["marks"]:
#             print(i)
#
#     display_key_values()
#     # display_marks()
#
#
# print(username)
# print_dict(name="Ronald", roll_number=12, address="USA", email="r@gmail.com", phone="+1236736281726", marks=[1,2,3,4,5])
# print(username)


###########################################################################################################################

# Second Example


# def calculate(number1):
#     def addition(number2):
#         return number2+number1
#
#     res = addition(2)
#     return res


# def calculate(number1, number2):
#     def addition(number2):
#         return number2+number1
#
#     res = addition(number2)
#     return res

# We can return the nested function from the parent function.

def calculate(number1):
    def addition(number2):
        return number2+number1

    # res = addition(2)
    # return res

    return addition


def main():
    # print(calculate(9, 2))
    # print(calculate(11, 5))

    temporary_function = calculate(9)
    print(temporary_function(2))
    print(temporary_function(6))

    temporary_function1 = calculate(11)
    print(temporary_function1(16))
    print(temporary_function1(18))

    print(temporary_function(3))


main()

###################################################################################################################

# Write a python program with nested functionality
# to get some name and roll number from the user
# and check there validity.
# name -> list
# roll number -> 1-40
# single global function
# We can call the nested function from the main function with some other values.

###################################################################################################################











