

# while

# While loops is used to iterate through something until the specific condition gives us a false value.

# while condition:
#   operation

# We have to write a program which gets valid integer from the user.

# while True:
#     try:
#         user_input = int(input("Enter number: "))
#         break
#     except:
#         print("Invalid input!!!")


# Write a program to print the numbers from 0 to 1000 skipping every second value using while loop.

# for i in range(0, 1000, 2):
#     print(i)

number = 0
# while number != 1000:
#     if number == 0:
#         print(number)
#         number = number + 2
#         print(number)
#     else:
#         number = number + 2
#         print(number)

# # 1)
# while number != 1000:
#     print(number)
#     number = number + 2
#
# # 2)
# while number != 1000:
#     if number % 2 == 0:
#         print(number)
#     number = number + 1
#
# number = -1
# # 3) continue
# while number != 1000:
#     number = number + 1
#     if number % 2 != 0:
#         continue
#     print(number)
#
#
# # Print numbers from 1-10 and skip the number 5
# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)


# Automation

# # 1)
# for i in range(5):
#     try:
#         print()
#     except:
#         print()
#
# # 2)
# for i in range(5):
#     print()
#     if "that element does not exist":
#         continue
#     print()
#     print()
#
#
# for i in range(5):
#     try:
#         try:
#             print()
#         except:
#             print()
#     except:
#         print()

#################################################################################################


# List Comprehension

# Shorten the syntax of iterating through list to make a new list.
# resultant_list = [expression for x in source_list]

# Write a program to copy each and every item from oe list to another.

numbers_list = [1, 2,3, 4,4, 5,56 ]
resultant_list = []
for x in numbers_list:
    resultant_list.append(x)




# resultant_list = numbers_list
#
# numbers_list[0] = 100
#
# print(resultant_list[0])


# Sort Lists
# Copy Lists
# Join Lists
#
# length,
# slicing,
# append,
# extend with other list,
# remove
# pop
# del list[0]
# del list
# clear()
# insert(2,value)
# sort() -> resulting in all capital letters being sorted before lower case letters
# sort(key = str.lower) -> for case insensitive
# sort(reverse=True)
# copy() or list(values as a list)
# make a copy with slice -> mylist = thislist[:]
# +
