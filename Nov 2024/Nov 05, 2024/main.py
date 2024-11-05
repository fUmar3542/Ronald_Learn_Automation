
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

# Input
check = False
sum_of_digits = 0

while True:
    try:
        user_input1 = int(input("Enter the first number: "))
        if user_input1 > 0:
            while True:
                try:
                    user_input2 = int(input("Enter the second number: "))
                    if user_input2 > 0:
                        if user_input2 > user_input1:
                            check = True
                            break
                        else:
                            print("Second number must be greater than the first number")
                    else:
                        print("Second number must be greater than 0")
                except:
                    print("ERROR! Enter the valid number")
            break
        else:
            print("First number should be greater than 0")
    except:
        print("ERROR! Enter the valid number")

if check:
    print(user_input1)
    print(user_input2)


# user_inputs = []
# for i in range(5):
#     # Get user input.
#     while True:
#         try:
#             user_input = int(input("Enter a number: "))
#             user_inputs.append(user_input)
#             check = True
#             break
#         except:
#             print("Enter a valid number.")




# Increment the range


# Sum each integer within a range


# Display the output

