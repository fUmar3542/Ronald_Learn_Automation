
##############################################
# Sorting of a list

# Ronald's solution

# 1) First get the smallest number from the list and store it in resultant list
# 2) Remove the smallest number from the numbers list
# 3) Repeat the same scenario


# Selection sort algorithm

# numbers_list = [32, 34, 5, 21, 78]
# # resultant_list = []
#
# if len(numbers_list) > 0:
#     smallest = 0
#     while numbers_list:
#         for i in range(len(numbers_list)):
#             if numbers_list[i] < numbers_list[smallest]:
#                 smallest = i
#         # resultant_list.append(numbers_list[smallest])
#         # numbers_list.pop(smallest)
#     print(numbers_list)
# else:
#     print("Input list is empty.")


###########################################
# Write a program to swap two numbers

# # Solution 1: with 1 temporary variable
# num1 = 23
# num2 = 56
#
# swap = num1
# num1 = num2
# num2 = swap
#
# print(num1)
# print(num2)

# Solution 2: without any additional variable
# Hint: You can do that simply with the help of arithmetic operations(+ and -)

# num1 = 23
# num2 = 56
#
# num1 = f"{num1}{num2}"
# num2 = num1
#
# print(num1)
# print(num2)


##############################################################
# Write a program to get a number from user and prints 101
# if the user is entering 100, but if the user is entering 101,
# we'll be printing 100
# We don't have to use the conditional statements
# Hint: You can do that simply with the help of arithmetic operations(+ and -)

# number = int(input("Enter number: "))
#
# print()




################################################
# Sorting

# Ascending
# numbers_list = [23,43,56,48,2]
# numbers_list.sort()
# print(numbers_list)


# Descending
numbers_list = [23,43,56,48,2]
numbers_list.sort(reverse=True)
print(numbers_list)



