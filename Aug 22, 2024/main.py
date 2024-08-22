

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

# # Solution
# ageInput = int(input('Enter age: '))
#
# if ageInput < 5:
#     print("Free")
#     print("First statement is checked")
# elif (ageInput >= 5) and (ageInput <= 12):
#     print("$10")
#     print("Second statement is checked")
# elif (ageInput >= 13) and (ageInput <= 17):
#     print("$15")
#     print("Third statement is checked")
# elif (ageInput >= 18) and (ageInput <= 59):
#     print("$20")
# else:
#     print("$10")
#
#
# # nested if
#
# if ageInput < 5:
#     print("Free")
#     print("First statement is checked")
# else:
#     if (ageInput >= 5) and (ageInput <= 12):
#         print("$10")
#         print("Second statement is checked")
#     else:
#         if (ageInput >= 13) and (ageInput <= 17):
#             print("$15")
#             print("Third statement is checked")
#         else:
#             if (ageInput >= 18) and (ageInput <= 59):
#                 print("$20")
#             else:
#                 print("$10")


#  Practice Question 02
# 2. Grading System
# Create a function that takes a student's score (out of 100) and returns their grade based on the following:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Additionally, include logic to return "Invalid score" if the score is not within the range of 0 to 100.

# Solution

# Input
scoreInput = int(input("Enter your score: "))

# Validation
if (scoreInput < 0) or (scoreInput > 100):
    print("Invalid score")
# Comparison -> conditional statements (elif)
elif scoreInput >= 90:
    print("A")
elif (scoreInput >= 80) and (scoreInput <= 89):
    print("B")
elif (scoreInput >= 70) and (scoreInput <= 79):
    print("C")
elif (scoreInput >= 60) and (scoreInput <= 69):
    print("D")
else:
    print("F")




# Home Work
# if type(scoreInput) != int



# 3. Leap Year Checker
# Write a Python program that determines whether a given year is a leap year. A year is a leap year if:
#
# It is divisible by 4, but not divisible by 100, unless
# It is also divisible by 400.
# The program should take a year as input and return whether it is a leap year.
#
#

# 4. Triangle Type
# Given the lengths of three sides of a triangle, determine whether the triangle is:
#
# Equilateral (all sides are equal)
# Isosceles (two sides are equal)
# Scalene (all sides are different)
# Not a valid triangle (the sum of any two sides must be greater than the third side)
#
# Write a function that takes the lengths of the three sides as input and returns the type of triangle.
#
#

# 5. Write a Python function to determine if a person is eligible for a loan based on the following criteria:
#
# The applicant must be at least 21 years old.
# The applicant must have a steady job with an annual income of at least $25,000.
# If the applicant is below 25 years old, they must have a co-signer.
# The applicant’s credit score must be above 600.
# The function should take the applicant’s age, income, job status (True/False), co-signer status (True/False), and credit score as inputs and return whether they are eligible for the loan.
