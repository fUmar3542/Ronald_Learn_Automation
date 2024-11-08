# Problem 2: Sum of Digits in a Range
# Write a program that takes two numbers, start and end, from the user and prints the sum of the digits for each number in that range. Use a for loop to iterate from start to end.

# Example:

# Input: 10 and 12
# Output:
# Sum of digits of 10 = 1
# Sum of digits of 11 = 2
# Sum of digits of 12 = 3

####################################################
# Solution


quantity = 2
temp = 0
check = 0
single_number_list = []
double_digit_list = []
numbers_list = []
ten_digit_sum = 0
result = 0

for i in range(quantity):
    while True:
        try:
            user_input = int(input(f"Enter number {i + 1}: "))
            if user_input > 0:
                if user_input > temp:
                    temp = user_input
                    numbers_list.append(user_input)
                    break
                else:
                    print("Number must be greater than the previous number")
            else:
                print(f"Number {i+1} must be greater than 0")
        except:
            print("Error: invalid number")
print("")


#############################################################
# Solution 2
# Dynamic solution

for num in range(numbers_list[0], numbers_list[-1] + 1):
    sum_of_digits = 0
    number = num
    while number != 0:
        # Get the last digit
        mod = number % 10
        # Add it to the sum of digits
        sum_of_digits = sum_of_digits + mod
        # Remove the last digit from the number
        number = number // 10

    print(f"Sum of Digit {num} = {sum_of_digits}")
