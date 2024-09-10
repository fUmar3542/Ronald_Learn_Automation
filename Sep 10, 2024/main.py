
# **********************************************
# split

# name = (input("Enter your address(Hint: only 10 words separated by a space): "))  # MuhammadUmar
# name = name.capitalize()
#
# # abc@coworking, ABC@coworking
#
# # space_index = name.find(' ')
# # starting_index = space_index + 1
# #
# # print(name.capitalize()[0:space_index])
# # print(name.capitalize()[starting_index::])
#
# split_name = name.split()   # -> [first_element, second_selement, ....]
# print(split_name[1])


# *******************************************************
# concatenation

# name1 = "Ronald"
# name2 = "Johnson"
# name3 = "Ronald"
#
# # print(name1 + " " + name2 + " " + name3)
# print(name1, name2, name3)


# *******************************************************
# formatting ->f notation

country = "United States"

address1 = f'My Address is this: House No. 02, {country}'
# address1 = address1.replace("country", country)

address2 = f'My Address is this: House No. 02, {country}'
# address2 = address2.replace("country", country)

address3 = f'My Address is this: House No. 02, {country}'
# address3 = address3.replace("country", country)

address4 = f'My Address is this: House No. 02, {country}'
# address4 = address4.replace("country", country)

address5 = f'My Address is this: House No. 02, {country}'
# address5 = address5.replace("country", country)

house_no = 2
address = "Address"

# print("First Address: My", address, " is this: House No. ", house_no, country)
print(f"First Address: My {address} is this: House No. {house_no}, {country}")


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

