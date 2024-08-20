

# Conditional Statements

# 1) If Statement

# number = 8

# Write program which gets input from user and prints greater than 5 on screen if the value given by user is greater than 5

userInput = int(input("Enter number: "))

# if userInput > 5:
#     print("Greater than 5")
#     print()
#     print()
#
# if userInput < 10:
#     print("Less than 10")
#
#
# if userInput == 8:
#     print("Input is equal to 8")
#
#
# # 2) else statement
#
# if userInput > 5:
#     print("Greater than 5")
#     print()
#     print()
# else:
#     print()

# print()


# Write a program which gets input fom user and checks if the input is greater than 5 and the input is less than 10,
# and user input is equal to 8
# then print acceptable otherwise print not acceptable

# 3) Nested if statement

if userInput > 5:
    if userInput < 10:
        if userInput == 8:
            print("Acceptable")
        else:
            print("Not Acceptable")
    else:
        print("Not Acceptable")
else:
    print("Not Acceptable")


# 4) Boolean conditional statement -> and or

if (userInput > 5) and (userInput < 10) and (userInput == 8):
    print("Acceptable")
else:
    print('Not Acceptable')


# Write a program which gets input fom user and checks if the input is greater than 5 and the input is less than 10,
# or user input is equal to 2
# then print acceptable otherwise print not acceptable

if ((userInput > 5) and (userInput < 10)) or (userInput == 2):
    print("Acceptable")
else:
    print('Not Acceptable')


# 5) elif statement -> else if

# Write a program which gets input fom user and checks if the input is greater than 5 and the input is less than 10,
# then print acceptable
# otherwise checks if user input is equal to 2
# then print acceptable otherwise print not acceptable


if (userInput > 5) and (userInput < 10):
    print("Acceptable")
elif userInput == 2:
    print("Acceptable")
else:
    print('Not Acceptable')



