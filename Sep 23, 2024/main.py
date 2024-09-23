

##############################################

# Loops

# go through the collection of data -> lists, tuple, sets, user defined data.


# For Loop

# Simple for loop with range keyword

# for i in range(0, length):
#     if numbers[i] == key:
#         numbers.remove(key)
#     print(numbers[i])

# resultant = []
# for i in range(0, length):
#     if numbers[i] != key:
#         resultant.append(numbers[i])
#
# print(resultant)

numbers = [23,54,56,76,87]
length = len(numbers)

# Advantages of creating the length variable

# 1) Reduce the time complexity
# 2) Readability
# 3) Re-usability

# for n in range(0, length):    # 0 > len(numbers), 1 > len(numbers), 2 > len(numbers)
#     print(numbers[n])


# Foreach loop

# If we have some condition, in which there is a need to go through each and
# every item of the data type, we can simply use the foreach loop there

# e.g display all the items of a list on console

# for item in numbers:
#     print(item)

# sum = 0
# for item in numbers:
#     sum += numbers
#
# print(sum)


# Problem
# Write a robust program to print all the items of a list on console
# without the second item using simple for loop and foreach loop as well.

# numbers = []
# Simple For loop solution

combine_to_list = []
# for n in range(0, length):
#     print(numbers[n])
#     combine_to_list.append(numbers[n])
#     break

print(numbers[0])

for n in range(2, length):
    print(numbers[n])
    combine_to_list.append(numbers[n])

print(combine_to_list)


# Foreach loop solution



# While loop
