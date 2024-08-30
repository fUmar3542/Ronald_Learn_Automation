

# 5. Write a Python program to determine if a person is eligible for a loan based on the following criteria:
#
# The applicant must be at least 21 years old.
# The applicant must have a steady job with an annual income of at least $25,000.
# If the applicant is below 25 years old, they must have a co-signer.
# The applicant’s credit score must be above 600.
#
# The function should take the applicant’s age, income, job status (True/False), co-signer status (True/False),
# and credit score as inputs and return whether they are eligible for the loan.

try:
    age = int(input("Enter age: "))
    if age < 21:
        print("Age should be greater than 20.")
    else:
        annualIncome = float(input("Enter annual income: "))
        if annualIncome < 25000:
            print("Annual income should be at least $25000.")
        else:
            coSigner = input("Enter co-signer(Hint: yes/no): ") # no
            if (age < 25) and (coSigner == 'no'):
                print("You must have a co-signer.")
            else:
                creditScore = int(input("Enter credit score: "))
                if creditScore <= 600:
                    print("You must have a credit score above 600.")
                else:
                    print("You are eligible for the loan.")

except Exception as ex:
    print("Incorrect input: " + str(ex))
else:
    print()


# 6. BMI Calculator
# Create a program that calculates a person's Body Mass Index (BMI) using their weight (in kilograms) and height (in meters). The BMI is calculated using the formula:
#
# BMI = weight / height^2
#
# The program should print the BMI category based on the following ranges:
#
# Underweight: BMI < 18.5
# Normal weight: 18.5 ≤ BMI < 24.9
# Overweight: 25 ≤ BMI < 29.9
# Obesity: BMI ≥ 30


# 7. Shipping Cost Calculator
# A company charges shipping based on the weight of the package and the delivery location. The rates are as follows:
#
# For packages up to 5 kg:
# Domestic: $5
# International: $15
#
# For packages between 5 and 20 kg:
# Domestic: $10
# International: $30
#
# For packages over 20 kg:
# Domestic: $20
# International: $50
#
# Write a Python function that takes the package weight and delivery location as inputs and returns the shipping cost.
#

#
# 8. Temperature Converter
# Create a Python program that converts temperatures between Fahrenheit and Celsius. The program should take two inputs:
# the temperature value and the unit of the temperature ("C" for Celsius or "F" for Fahrenheit). The program should print the converted temperature in the other unit.
