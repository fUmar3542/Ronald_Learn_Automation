
# score = input("Enter your score: ")
#
# grade = ""
#
# try:
#     score = int(score)
#     score = float(score)
#     print("Something" + None)
#     # multiple lines
#     # multiple lines
# except Exception as ex:
#     # print("The input given is not a number")
#     print(ex)
#     grade = "None"
#     pass
#
# print(grade)

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



# Input
scoreInput = input("Enter your score: ")

try:
    scoreInput = float(scoreInput)
except Exception as ex:
    print("Invalid input. Please enter a valid score value as a number or a decimal value")
else:
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
