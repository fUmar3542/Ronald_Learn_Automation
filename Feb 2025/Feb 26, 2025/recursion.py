

#########################################################################################################

# Recursion

# Basic types of recursions in Python

# 1) Tail recursion
# We'll be calling a recursive function following the tail recursion in case if the recursive call
# is the last statement in that function


# Print natural numbers in an ascending order
def print_natural_number(number, count=1):
    if number < count:
        return
    # print(count)
    print_natural_number(number, count+1)


print_natural_number(7)

numbers = [[1,2,3,4], [5,6,7,8]]

# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         print(numbers[i][j])


# 2) Non-tail recursion
# We'll be calling a recursive function following the non tail recursion in case if the function
# is also performing some calculation with the recursive call


# Write a program to calculate the sum of the numbers from 1 to the number accepted as a parameter

def sum(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum


# def recursive_sum(number):
#     sum = 0
#     final_sum = 99999999
#     if sum == final_sum:
#         return sum
#     result = recursive_sum(1, number)
#     final_sum = sum + result
#     return final_sum


def recursive_sum(number):
    if number == 0:
        return 0
    return number + recursive_sum(number - 1)

# 5 + recursive_sum(4) = 5 + 10 = 15
# 4 + recursive_sum(3) = 4 + 6 = 10
# 3 + recursive_sum(2) = 3 + 3 = 6
# 2 + recursive_sum(1) = 2 + 1 = 3
# 1 + recursive_sum(0) = 1 + 0 = 1
# return 0


print(recursive_sum(5))


