

# 5. Write a Python program to determine if a person is eligible for a loan based on the following criteria:
#
# The applicant must be at least 21 years old.
# The applicant must have a steady job with an annual income of at least $25,000.
# If the applicant is below 25 years old, they must have a co-signer.
# The applicant’s credit score must be above 600.

# The function should take the applicant’s age, income, job status (True/False), co-signer status (True/False),
# and credit score as inputs and return whether they are eligible for the loan.

try:
    coSigner = input("Enter co-signer(Hint: yes/no): ")
    creditScore = int(input("Enter credit score: "))
    if creditScore >= 600:
        age = int(input("Enter age: "))
        if age > 24 and coSigner == "yes":
            annualIncome = float(input("Enter annual income: "))
            if annualIncome > 24999:
                print()
            else:
                print("Annual income should be at least $25,000.")
        else:
            print("Age input should be greater than 20.")
    else:
        print("")
except Exception as ex:
    print("Incorrect input: " + str(ex))
else:
    print()

