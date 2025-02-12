
# ------------------------------------------------------------------------------

# 5) Function with return statement


value1 = value2 = 12


# Write a function which find and return the sum of the two numbers.


def sum_numbers(value1, value2):
    return value1 + value2


result = sum_numbers(12, 67)


# Can we return multiple values from the function?

# Write a function which will be accepting two parameters and it'll be
# return the sum, multiplication, division and subtraction of these values.

def calculations(value1, value2):
    return value1+value2, value1*value2, value1/value2, value1-value2


# result1 = calculations(14, 10)      # result1 -> Tuple
#
# result1, result2, result3, result4 = calculations(14, 10)   # Store values in equal number of variables
#
# result1, *result2 = calculations(14, 10)    # result1 -> variable, result2 -> list
#
# print(result1, result2, result3)


# ------------------------------------------------------------------------------------------------------------

# Write a program which will be getting the name and id of the student. write a function for that.
# Do some exception handling. This function will also return the id and name of the student.


# After getting the user input in main function, we'll be doing validity check on name and id,
# we'll creating a validity_check function which will return True in case if the id is between
# 1 and 100 and name is present in our list, otherwise return False.
