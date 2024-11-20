###########################################################
# We have to find and print the smallest number in the list
###########################################################

# Solution 1

# numbers_list = [32, 34, 5, 21, 78]
#
# smallest = -1
# smallest_list = []
#
# for i in range(0, len(numbers_list)):
#     for j in range(len(numbers_list)):
#         if numbers_list[i] < numbers_list[j]:
#             smallest = numbers_list[i]
#             smallest_list.append(smallest)
#             for x in range(len(smallest_list)):
#                 if smallest_list[x] < smallest:
#                     smallest = smallest_list[x]
# print(smallest)

########################################################
# Solution 2

# numbers_list = [32, 34, 5, 21, 78]
#
# if len(numbers_list) > 0:
#     smallest = numbers_list[0]
#     for i in range(len(numbers_list)):
#         if numbers_list[i] < smallest:
#             smallest = numbers_list[i]
# else:
#     print("Input list is not valid.")



##############################################
# Sorting of a list

# Ronald's solution

# 1) First get the smallest number from the list and store it in resultant list
# 2) Remove the smallest number from the numbers list
# 3) Repeat the same scenario


# Selection sort algorithm

numbers_list = [32, 34, 5, 21, 78]
resultant_list = []

if len(numbers_list) > 0:
    smallest = 0
    while numbers_list:   # while len(numbers_list) > 0:
        for i in range(len(numbers_list)):
            if numbers_list[i] < numbers_list[smallest]:
                smallest = i
        resultant_list.append(numbers_list[smallest])
        numbers_list.pop(smallest)
    print(resultant_list)
else:
    print("Input list is empty.")


# if check:          ->  if check == True:
# if str:            ->  if len(str) > 0:
# if numbers_list:   ->  if len(numbers_list) > 0:
