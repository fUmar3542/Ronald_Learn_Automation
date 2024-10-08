import random

# Practice Question 1 -> You have to write a program in which you have to get an integer from user
# and you have to generate an integer with the help of random library and you have to display them both on console.

# # Practice question 1 solution
#
# userInput = input("Enter an integer: ")
# userInput = int(userInput)
#
# # print(type(userInput))
#
# generatedInteger = random.randrange(1,7)
#
# print(userInput)
# print(generatedInteger)
#
# print(userInput, generatedInteger)


# Practice Question 2 -> How to generate a unique number in a specified range with the help of random?

# number1 = random.randrange(1,7)
# number2 = random.randrange(1,7)
# number3 = random.randrange(1,7)
#
# print(number1, number2, number3)


numbers = random.sample(range(1,7), 3)

print(numbers)


# Practice # 3

# Write a Python script that simulates a simple lottery game. The script should do the following:

# 1) Generate a Winning Number:
    # Use the random library to generate a random 6-digit number (each digit should be between 0 and 9).

# 2) User Input:
    # Ask the user to input a 6-digit number as their lottery ticket.

# 3) Print both numbers on console
