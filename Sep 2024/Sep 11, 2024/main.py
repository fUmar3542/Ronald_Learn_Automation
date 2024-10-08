
# String Functions

# *******************************************************
# formatting ->f notation

country = "United States"

house_no = 2
address = "Address"

# print("First Address: My", address, " is this: House No. ", house_no, country)
# print(f"First Address: My {address} is this: House No. {house_no}, {country}")
# print("First Address: My" +  address + " is this: House No. " + str(house_no) + " " + country)

height = 5.7883246

# print("My height is: " + str(height * 5))
# print("My height is: ", height*5)
# print(f"My height is: {height*5:.2f}")


# *******************************************************
# count() -> count some character

fruit = "BANANA"
# [first_element, second_element, ...]
print(fruit.lower().count('a'))

# *******************************************************
# islower()

if fruit[0:3].islower():
    print("Lower case")

# *******************************************************
# isupper()

if fruit[0:3].isupper():
    print("Upper case")

# *******************************************************
# find()
# rfind()
# index()

fruit_lower = fruit

# print(fruit_lower.index('a'))
#
# # rindex()
#
# print(fruit_lower.rindex('a'))

# Difference between find and index

print(fruit_lower.find('a'))
print(fruit_lower.find('A'))

print(fruit_lower.index('A'))


# *******************************************************
# isalpha()

if fruit.isalpha():
    print("All alphabets")


# *******************************************************
# isnumeric()

number = "234"
if number.isnumeric():
    print("Numeric")

# *******************************************************
# isspace()

spaces = "    "
if spaces.isspace():
    print("Spaces")


# ********************************************************
# Practice Questions

# 1) Username Validator: Write a program that checks if a given username is valid. A valid username should:
#
# Be between 5 and 15 characters long,
# Only contain letters and digits (no special characters),
# Start with a letter.
# If the username meets all the conditions, print "Valid username"; otherwise, print "Invalid username."


# 2) License Plate Validator: Write a program that checks if a given license plate number is valid. A valid license plate should:
#
# Be exactly 7 characters long,
# Contain only uppercase letters and digits,
# Start with 3 letters and end with 4 digits.
# If the license plate meets these conditions, print "Valid license plate"; otherwise, print "Invalid license plate."


# 3) Credit Card Validator: Write a program that checks if a given credit card number is valid. A valid credit card number should:
#
# Be exactly 16 digits long,
# Start with either 4, 5, or 6,
# Not contain any spaces or special characters.
# If the credit card number is valid, print "Valid credit card number"; otherwise, print "Invalid credit card number."
