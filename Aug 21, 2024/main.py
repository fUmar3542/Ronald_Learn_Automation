

# c++
# int number; -> variable declaration
# number = 5; -> variable assignment

# int number = 5; -> variable initialization


# Conditional Statement


# 6) Ternary operator

# Write a program which gets input number from user which assign "greater than"
# to check variable in case if the value is greater than 10 otherwise assign "less than" to check variable

# userInput = int(input("Enter number: "))
#
# # check = ""
#
# if userInput > 10:
#     check = "greater than"
# else:
#     check = "less than"
#
# print(check)
#
# # check = "equal"
# #
# check = "greater than" if (userInput > 10) else "less than"


# Practice question 1
# Age-Based Discounts
# You are designing a ticketing system for a theme park. The pricing is as follows:
#
# Children under 5 get in for free.
# Children between 5 and 12 years old pay $10.
# Teenagers between 13 and 17 years old pay $15.
# Adults between 18 and 59 years old pay $20.
# Seniors 60 years and older get a 50% discount on the adult price.
#
# Write a Python program that takes a person's age as input and returns the ticket price they need to pay.

# Solution
ageInput = int(input('Enter age: '))

if ageInput < 5:
    print("Free")
print("First statement is checked")

if (ageInput >= 5) and (ageInput <= 12):
    print("$10")
print("Second statement is checked")

if (ageInput >= 13) and (ageInput <= 17):
    print("$15")
print("Third statement is checked")

if (ageInput >= 18) and (ageInput <= 59):
    print("$20")
else:
    print("$10")
