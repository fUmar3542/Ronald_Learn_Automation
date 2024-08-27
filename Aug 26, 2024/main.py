

# Exception Handling -> try, except, else, finally

score = input("Enter your score: ")

grade = ""

try:
    score = int(score)
    score = float(score)
    print("Something" + None)
    # multiple lines
    # multiple lines
except:
    # print("The input given is not a number")
    grade = "None"
else:
    grade = "A"
finally:
    print("Grade: " + grade)


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


# 5. Write a Python function to determine if a person is eligible for a loan based on the following criteria:
#
# The applicant must be at least 21 years old.
# The applicant must have a steady job with an annual income of at least $25,000.
# If the applicant is below 25 years old, they must have a co-signer.
# The applicant’s credit score must be above 600.
# The function should take the applicant’s age, income, job status (True/False), co-signer status (True/False), and credit score as inputs and return whether they are eligible for the loan.
