

###############################################################################
# Reverse a number program
# Write a python program to print the reverse of an int number given by the user
###############################################################################


# Variables
check = False
reversed_list = []

# Input

# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         check = True
#         break
#     except:
#         print("Enter a valid number.")

# Reverse

# Solution 2
# result = ""
# if check:
#     user_input_string = str(user_input)
#     length = len(user_input_string)
#     for i in range(length):
#         i = i + 1
#         reversed_int = user_input_string[-i]
#         result = result + reversed_int

# print(result)

# Solution 3

# Input

while True:
    try:
        user_input = int(input("Enter a number: "))
        check = True
        break
    except:
        print("Enter a valid number.")
result = 0

while user_input != 0:
    # # Find a remainder
    # number2 = user_input % 10
    # Append it to result
    result = result * 10 + (user_input % 10)
    # Divide the nuber by 10
    user_input = user_input // 10

print(result)

# number2 = number % 10
# result = result * 10 + number2
#
# number2 = number % 10
# result = result * 10 + number2
#
# print(result)


# 56 4 = 564
# 56 * 10 + 4 = 564
#
# 564 2
# 564 * 10 + 2 = 5642
#
# 5642 1
# 5642 * 10 + 1 = 56421

# reverse = 5 * 10 + 6
#
# print(number)



####################################################################
# Home work

# Armstrong number
# Write a python program to check if a number is an armstrong number
####################################################################

# 16 = 1^3 + 6^3 = 1*1*1 + 6*6*6 = 217
# 153 = 1 + 125 + 27 = 153

number = 123
