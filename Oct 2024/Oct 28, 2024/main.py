

# While Loop

# We'll be using this loop in which we don't know the number of iterations.

# while condition:
#     loop body

# x = 0
# while x < 3:
#     print("Hello")
#     x = x + 1

# x = 0
# while True:
#     x = x + 1
#     if x == 3:
#         break
#     print("Hello")


#############################################################
# Practice Question
# Write a python program to get an input number from the user
# until he enters 0.

## Solution 1

# user_input = 1
# while user_input != 0:
#     try:
#         user_input = int(input("Enter a number: "))
#     except:
#         print("ERROR! Please enter a valid number.")


## Solution 2
while True:
    try:
        user_input = int(input("Enter a number: "))
        if user_input == 0:
            break
    except:
        print("ERROR! Please enter a valid number.")


############################################################
# Home Work
# Write a python program to get int or float from the user
# until the user enters 0. When the user will be writing 0,
# you'll be printing the largest, the smallest and the sum of
# all the numbers.
############################################################



# 1) initialization -> i = 0/value
# 2) condition -> if i < 3, if i != 3
# 3) increment/decrement

# for i in range(3):
#     print("Hello")

# for i in range(100):
#     print("Hello")
#     if i == 50:
#         break
