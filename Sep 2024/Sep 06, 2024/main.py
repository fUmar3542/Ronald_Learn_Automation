

# 3) Ask the user for their email. Check if it contains both "@" and "."
# and print "Valid email" if both are present, otherwise print "Invalid email."


# == -> left value, right value
# abc == dbc
# is
# in -> "Programming program gram" "rogram"

user_email_input = input("Enter your email: ")

# print(user_email_input[-4])

if user_email_input[-4] == '.' and '@' in user_email_input:
    print("Valid email.")
else:
    print("Invalid email.")


# **********************************************************

name = "Joe Johnson JohnsonJ"

leading_index = name.find('Johnson')    # left to right
trailing_index = name.rfind("Johnson")  # right to left

print(leading_index, trailing_index)


# ronald.johnson.johnson.johnson@gmail.gma.io
