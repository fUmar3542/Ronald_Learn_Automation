
##############################################
# Sorting of a list

# Ronald's solution

# 1) First get the smallest number from the list and store it in resultant list
# 2) Remove the smallest number from the numbers list
# 3) Repeat the same scenario

# num1, num2 = num2, num1

# Selection sort algorithm
# Find the smallest number index in each iteration, then swap the numbers using smallest and iteration number index

numbers_list = [32, 34, 5, 21, 78]

# smallest = 2
# [5, 34, 32, 21, 78]

# smallest = 4
# [5, 21, 32, 34, 78]

# smallest = 2
# [5, 21, 32, 34, 78]

# smallest = 3
# [5, 21, 32, 34, 78]

# smallest = 4
# [5, 21, 32, 34, 78]

# range(5) == range(0, 5)

if len(numbers_list) > 0:
    for index in range(len(numbers_list)):
        # Find the smallest number
        smallest = index
        for i in range(index, len(numbers_list)):
            if numbers_list[i] < numbers_list[smallest]:
                smallest = i
        # Swap
        numbers_list[index], numbers_list[smallest] = numbers_list[smallest], numbers_list[index]

    print(numbers_list)
else:
    print("Input list is empty.")


# Bubble Sort Algorithm

# numbers_list = [32, 34, 5, 21, 78]
#
# if len(numbers_list) > 0:
#     for i in range(len(numbers_list)):
#         if numbers_list[i] > numbers_list[i + 1]:
#             numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
#
#     print(numbers_list)
# else:
#     print("Input list is empty.")
