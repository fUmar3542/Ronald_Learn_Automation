import random

# How to comment out or uncoment the code in Pycharm
# Ctrl + / key


# randrange vs randint

# Differences
# 1) randrange(1,7) -> randrange (1 inclusive while 7 exclusive)
# 2) randint(1,7) -> randint(1 and 7 are both inclusive)
# 3) step value -> randrange has a step value but randint don't have that functionality
#   # Write a program to generate a random odd number between 1 and 10 (10 exclusive)?

# # example
# number = random.randrange(1, 10, 1) # -> 1,2,3,4,5,6,7,8,9
# # solution
# number = random.randrange(1, 10, 2) # -> 1,3,5,7,9


# Practice # 3

# Write a Python script that simulates a simple lottery game. The script should do the following:

# 1) Generate a Winning Number:
    # Use the random library to generate a random 6-digit number (each digit should be between 0 and 9).

# 2) User Input:
    # Ask the user to input a 6-digit number as their lottery ticket.

# 3) Print both numbers on console


# # Solution
# # First part
# # 0, 00, 000, 000001, 100000
# number = random.randint(100000, 999999)
#
# # Second part number
# inputNumber = input("Enter a 6 digit number: ")


# # Operators
# Arithmetic operators -> + - * /
# Assignment operators -> = += *=
# Comparison operators -> == != > < >= <=
# Logical operators -> and or
# Identity operators -> is
# Membership operators -> in
# Bitwise operators & |
#
#
# Operator precendence
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or	OR


# Arithematic operators
add = 2 + ((7 - 10) * (6 + 9)) + 9
print(add)

number1 = 10
number2 = 2

print(number1 * number2)


# Practice question -> You have to write a program which will print the square of number getting as an input from user. (Hint: Arithematic operator)




