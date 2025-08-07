print()
# some_function()

# Recursive function
# A function which can call itself to do a particular task recursively.

# Base Condition
# A condition which is used to break the recursion.
# The recursive calls will be returned once the base condition is met.

# def recursive_function():
#     if base_condition:
#         return
#     recursive_call


number = 89
# print(number)
# print(number-1)
# print(number-2)

while True:
    if number == 0:
        break
    print(number)
    number = number -1


# return statement

def validate(email):
    if "@" in email:
        return True
    return False


def get_input():
    email = input("Enter an email: ")
    check = validate(email)
    if check:
        print("Valid input")
    return


get_input()
print("Function Execution Done.")


# sdkjsdkj
# kjefkwkf
# hjswbkfwekjf
# bbwej


# Stack
# LIFO
# Last In First Out


