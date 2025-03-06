

# Lists -> ordered & changeable
# changeable, allow duplicates
# mutable -> if structure is changeable

numbers_list = [1, 2, 33, 2123, 2]


# Access List Items

# Indexing
print(numbers_list[0])

# Change List Items

numbers_list[0] = 45


# Add List Items

# append
# add items to the end

numbers_list.append(89)

print(numbers_list[-1])


# insert

print(numbers_list)

numbers_list.insert(0, 100)

print(numbers_list)


# Remove List Items

# del
# del value at particular index
del numbers_list[0]

# pop
# pop value at particular index
numbers_list.pop(0)

# remove
# remove the specified value
numbers_list.remove(2)

###########################################################################################################

# # Loops

# Types of loops

# 1. For Loop

# For some specific instance

# Types of for loop

# 1) for range loop

# Iterate through something n number of times

# range(starting_range, ending_range, step_value)

# starting and step value is not necessary to mention
# ending range is necessary to mention

# starting range is inclusive
# ending range is exclusive

# single number will be considered as an ending range
# implicitly the starting range is defined as 0.
range(12)

# two values in range
# starting and ending range
range(1, 10)

# 3 values in range

# step value 1
range(1, 10, 1)

# 1
# 1 + 1 -> 2
# 2 + 1 -> 3
# ...
# 8 + 1 -> 9

# step value 3
range(1, 10, 3)
# 1
# 1 + 3 -> 4
# 4 + 3 -> 7


for index in range(2,10,2):
    print(index * index)


numbers_list = [1, 2, 33, 2, 34, 32]

# print(numbers_list[0])
# print(numbers_list[1])
# print(numbers_list[2])
# print(numbers_list[3])
# print(numbers_list[4])

# print(len(numbers_list))

for i in range(len(numbers_list)):
    print(i, numbers_list[i])

print("---------------------------------------------------")

# 2) for each loop

# Iterate through each item of some collection

numbers_list = [1,2,3,4,45,6]

for index, item in enumerate(numbers_list):
    print(index, item)

index = 0
for item in numbers_list:
    print(index, item)
    index = index + 1


