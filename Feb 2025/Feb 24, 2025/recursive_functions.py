
#####################################################################################################

# Recursion
# I want to execute some script again and again by calling it only once.

# Recursive Functions
# It is also the type of function in which I am calling the function once and it'll call the
# same function automatically until the base case fails.

# Base Case
# The condition to break/stop the recursion.

# Parts of the recursive function
# 1) Function Header
# 2) Function Body
#    i. Base case
#    ii. Recursive call to the same function


# Write a program to print the natural numbers on console as given by the user as input.

def print_natural_numbers(number):
    for i in range(1, number+1):
        print(i)


# print_natural_numbers(20)


def print_natural_number(number):
    if number == 0:
        return
    print(number)
    print_natural_number(number - 1)


print_natural_number(5)
