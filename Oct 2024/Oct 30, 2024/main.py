#
# # Homework
# # Write a python program to get int or float from the user
# # until the user enters 0. When the user will be writing 0,
# # you'll be printing the largest, the smallest and the sum of
# # all the numbers.
#
#
# # sentinel_value = 0
# # input_sum = 0
# # largest_number = 0
# # smallest_number = 0
# # iteration_number = 0
#
# # Solution # 2
# sentinel_value = input_sum = largest_number = smallest_number = iteration_number = 0
#
# while True:
#     try:
#         user_input = float(input("Enter a number: "))
#         if user_input == sentinel_value:
#             break
#         if iteration_number == 0:
#             smallest_number = user_input
#             largest_number = user_input
#             iteration_number = 1
#         input_sum = input_sum + user_input
#         if user_input > largest_number:
#             largest_number = user_input
#         if user_input < smallest_number:
#             smallest_number = user_input
#     except:
#        print(f"Error: please enter a valid number other than {sentinel_value}")
#
# # Solution # 1
# # while user_input != sentinal_value:          # Sentinal value
# #     try:
# #         user_input = float(input("Enter a number: "))
# #         if iteration_number == 0:
# #             smallest_number = user_input
# #             largest_number = user_input
# #             iteration_number = 1
# #         if user_input != sentinal_value:
# #             input_sum = input_sum + user_input
# #             if user_input > largest_number:
# #                 largest_number = user_input
# #             if user_input < smallest_number:
# #                 smallest_number = user_input
# #     except:
# #         print("Error: please enter a valid number")
#
# print("")
# print(f"Sum: {input_sum}")
# print(f"Largest Number: {largest_number}")
# print(f"Smallest Number: {smallest_number}")


###############################################################################
# Reverse a number program
# Write a python program to print the reverse of a int number given by the user
###############################################################################

# Solution

check = False
# Input
while True:
    try:
        user_input = int(input("Enter a number: "))
        check = True
        break
    except:
        print("Enter a valid number.")

# Reversing

# Solution 1
# if check:
#     user_input = str(user_input)[::-1]

# Solution 2
modified_input = str(user_input)
length = len(modified_input)
for i in range(length):
    print(modified_input[length - 1])



# Display
print(user_input)
