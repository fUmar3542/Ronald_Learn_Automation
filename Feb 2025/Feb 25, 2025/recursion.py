

# Print natural numbers in a reverse order
# def print_natural_number(number):
#     if number == 0:
#         return
#     print(number)
#     print_natural_number(number - 1)
#
#
# print_natural_number(5)


# # Print natural numbers in an ascending order
# def print_natural_number(number):
#     if number == 0:
#         return
#     print_natural_number(number - 1)
#     print(number)


# Print natural numbers in an ascending order
def print_natural_number(number, count=1):
    if number < count:
        return
    print(count)
    print_natural_number(number, count+1)


print_natural_number(7)
