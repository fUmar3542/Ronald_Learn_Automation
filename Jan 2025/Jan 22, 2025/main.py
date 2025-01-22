

# Sorting

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


# Selection sort

# Finding the smallest number and we'll be placing it in the iteration location

numbers = [5, 3, 2, 7, 3, 1, 4, 3]

for j in range(len(numbers)):
    smallest_index = j
    for i in range(len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i
    numbers[j], numbers[smallest_index] = numbers[smallest_index], numbers[j]

print(numbers)
