

# nested functions


def print_user():
    print()


def get_input():
    a = 12


def print_and_get_input():

    def get_input():
        a = 12

    def print_user():
        print()

    print_user()


print_and_get_input()


def calculator(val1: float, val2: float, operation: str) -> float:

    def division():
        if val2 != 0:
            return val1 / val2
        else:
            return 0

    if operation == "+":
        return val1 + val2
    elif operation == "-":
        return val1 - val2
    elif operation == "*":
        return val1 * val2
    else:
        return val1 / val2



calculator(5, 10, "+")


#######################################################################################################

# Problem 1: Student Grading System with Validation and Reporting
# Problem Statement:
# Create a function grade_students(data) which accepts a list of student dictionaries containing names and marks.
# The function should:
# 	1	Validate each student's marks using a nested function validate().
# 	2	Assign grades using another nested function assign_grade().
# 	3	Print a report of students with their grades.
# Sample Input:
# students = [
#     {"name": "Alice", "marks": 85},
#     {"name": "Bob", "marks": 73},
#     {"name": "Charlie", "marks": 102},  # Invalid
#     {"name": "Dave", "marks": 60}
# ]
#
# Expected Output:
# Alice: Grade A
# Bob: Grade B
# Invalid marks for Charlie: 102
# Dave: Grade C


#######################################################################################################

def grade_students(data):
    print()



data = []
grade_students(data)



# lambda
# recursion
# high order functions
# @decorator
# pass by value vs pass by reference
# shallow copy vs deep copy