

# Bubble sort

# Finding the largest number and placing it in the last location in ach iteration
#
# numbers = [5, 1, 2, 7, 3, 4, 3]
#
# # [1,5,...]
# # [1,2,5,..]
#
# for j in range(len(numbers)):
#     # find the largest number
#     for i in range(0, len(numbers) - j - 1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#
# print(numbers)


##############################################################################
# Selection sort

# Finding the smallest number and we'll be placing it in the iteration location

numbers = [5, 3, 2, 7, 3, 1, 4, 3]

for j in range(len(numbers)):
    smallest_index = j
    for i in range(j+1, len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i
    numbers[j], numbers[smallest_index] = numbers[smallest_index], numbers[j]

print(numbers)


##################################################################


# # Swapping the numbers

# numbers = [5, 3, 2, 7, 3, 1, 4, 3]

# # 1st method to swap the values
# temp = numbers[0]       # temp = 5
# numbers[0] = numbers[5] # numbers[0] = 1
# numbers[5] = temp       # numbers[5] = 5

# # 2nd method to swap the values
# numbers[0], numbers[5] = numbers[5], numbers[0]

# # x = 10
# # y = 20
# # z = 5

# # x, y, z = 10, 20, 5

# print(numbers)
