# Problem 2: Sum of Digits in a Range
# Write a program that takes two numbers, start and end, from the user and prints the sum of the digits for each number in that range. Use a for loop to iterate from start to end.

# Example:

# Input: 10 and 12
# Output:
# Sum of digits of 10 = 1
# Sum of digits of 11 = 2
# Sum of digits of 12 = 3

####################################################
# Solution

# check = False
# sum_of_digits = 0
#
# while True:
#     try:
#         user_input1 = int(input("Enter first number: "))
#         if user_input1 > 0:
#             while True:
#                 try:
#                     user_input2 = int(input("Enter second number: "))
#                     if user_input2 > 0:
#                         if user_input2 > user_input1:
#                             check = True
#                             break
#                         else:
#                             print("Second number must be greater than the first number")
#                     else:
#                         print("Enter a number greater than 0")
#                         try:
#                             user_input2 = int(input("Enter second number: "))
#                         except:
#                             print("Error: invalid number.")
#                 except:
#                     print("Error: invalid number")
#             break
#         else:
#             print("Enter a number greater than 0")
#     except:
#         print("Error: enter a positive integer.")
#
# if check:
#     print(user_input1)
#     print(user_input2)

quantity = 2
temp = 0
numbers_list = []
for i in range(quantity):
    while True:
        try:
            user_input = int(input(f"Enter number {i + 1}: "))
            if user_input > 0:
                if user_input > temp:
                    temp = user_input
                    numbers_list.append(user_input)
                    break
                else:
                    print("Number must be greater than the previous number")
            else:
                print(f"Number {i+1} must be greater than 0")
        except:
            print("Error: invalid number")

for num in range(numbers_list[0], numbers_list[-1] + 1):
    sum_of_digits = 0
    if num > 9:
        last_digit = sum_of_digits + num % 10
        first_digit = num // 10
        last_digit + first_digit


# for i in range(numbers_list[-1] - numbers_list[0] + 1):
#     print()


# #########################################################
# # Previous solution
# check = False
# sum_of_digits = 0
# integer_list = []
# user_input_list = []
# user_input = ""
# quantity = 0
# greater_than = False
#
# i = 1
#
# # while True:
# #     try:
# #         quantity = int(input("How many numbers to enter?: "))
# #         if quantity > 0:
# #             check = True
# #             break
# #     except:
# #         print("Error: enter a valid number of entries")
#
# # for i in range(quantity):
# #     try:
# #         user_input = int(input("Enter a number?: "))
# #         integer_list.append(user_input)
# #         sum_of_digits = sum_of_digits + user_input % 10
# #         user_input = user_input // 10
# #         sum = sum_of_digits + user_input
# #         user_input_list.append(sum)
# #     except:
# #         print("Error: enter a valid number")
# #
# # print(integer_list)
# # print(user_input_list)
