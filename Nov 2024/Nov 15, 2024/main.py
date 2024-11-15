
# Write a program to get 2 integers from user


# Pseudo code

# Apply while loop to get the valid input from user
# get the first number from user and store it into number1 variable
# If the user input is a valid integer then move ahead, otherwise display an error message
# Apply while loop to get the valid input from user
# get second number from user and store it into number2 variable
# If the user input is a valid integer then move ahead, otherwise display an error message

count = 2
numbers_list = []
for i in range(count):
    while True:
        try:
            number1 = input(f"Enter number {i+1}")
            number1 = int(number1)
            numbers_list.append(number1)
            break
        except:
            print("Invalid input.")

# while True:
#     try:
#         number2 = input("Enter second number")
#         number2 = int(number2)
#         break
#     except:
#         print("Invalid input.")
