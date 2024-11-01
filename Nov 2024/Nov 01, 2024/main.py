
####################################################################
# Home work

# Armstrong number
# Write a python program to check if a number is an armstrong number
####################################################################

# 16 = 1*1*1 + 6*6*6 = 217
# 153 = 1 + 125 + 27 = 153
check = False
result = 0
number = 0
remainder = 0

# Get user input.
while True:
    try:
        user_input = int(input("Enter a number: "))
        check = True
        break
    except:
        print("Enter a valid number.")

# Check if user input is an armstrong number.
result = user_input
sum = 0
if check:
    while result != 0:
        remainder = result % 10
        cube = remainder ** 3
        sum = sum + cube
        result = result // 10
    if user_input == sum:
        print("Armstrong number")
    else:
        print("Not an armstrong number")



############################################################
# Write a program to print the sum of the digits of a number
############################################################

# 1234 = 1 + 2 + 3 + 4 = 10

# sum = 0
# # Get user input.
# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         check = True
#         break
#     except:
#         print("Enter a valid number.")
#
# if check:
#     while user_input!= 0:
#         remainder = user_input % 10
#         sum = sum + remainder
#         user_input = user_input // 10
#
# print(sum)



