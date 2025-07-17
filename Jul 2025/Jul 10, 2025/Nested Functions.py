

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

# Database
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 73},
    {"name": "Charlie", "marks": 102},  # Invalid
    {"name": "Dave", "marks": 60}
]

# Operation
# 1) Validate the marks of students
# 2) Assign the grades

# Output
# report


# 1)

# # validate
# # 1.
# for student in students:
#     marks = student["marks"]
#     if marks >= 0 and marks <= 100:
#         if marks > 89:
#             grade = "A"
#         elif marks > 79 and marks < 90:
#             grade = "B"
#         elif marks > 69 and marks < 80:
#             grade = "C"
#         elif marks > 59 and marks < 70:
#             grade = "D"
#         else:
#             grade = "F"
#     else:
#         grade = "Invalid mark"
#     student["grade"] = grade
#
# # Output
# for x in students:
#     print(x)



# # 2)
#
# # validate
# # 1.
# def validate_and_mark(data):
#     for student in data:
#         marks = student["marks"]
#         if marks >= 0 and marks <= 100:
#             if marks > 89:
#                 grade = "A"
#             elif marks > 79 and marks < 90:
#                 grade = "B"
#             elif marks > 69 and marks < 80:
#                 grade = "C"
#             elif marks > 59 and marks < 70:
#                 grade = "D"
#             else:
#                 grade = "F"
#         else:
#             grade = "Invalid mark"
#         student["grade"] = grade
#
#     # Output
#     for x in data:
#         print(x)
#
#
# school1 = [
#     {"name": "Alice", "marks": 85},
#     {"name": "Bob", "marks": 73},
#     {"name": "Charlie", "marks": 102},  # Invalid
#     {"name": "Dave", "marks": 60}
# ]
#
# school2 = [
#     {"name": "Ronald", "marks": 80},
#     {"name": "Johnson", "marks": 90},
#     {"name": "Umar", "marks": 607},  # Invalid
#     {"name": "Farooq", "marks": 75}
# ]
# #
# # list_of_schools = ["school1", "school2"]
# #
# # for x in list_of_schools:
# #     validate_and_mark()
#
#
# validate_and_mark(school1)
# validate_and_mark(school2)


# 3)

# validate
# 1.
def validate_and_mark(data):
    # Validate
    # Assign grade
    for student in data:
        marks = student["marks"]
        if marks >= 0 and marks <= 100:
            if marks > 89:
                grade = "A"
            elif marks > 79 and marks < 90:
                grade = "B"
            elif marks > 69 and marks < 80:
                grade = "C"
            elif marks > 59 and marks < 70:
                grade = "D"
            else:
                grade = "F"
        else:
            grade = "Invalid mark"
        student["grade"] = grade

    # Output
    def output():
        for x in data:
            print(x)

    def run():
        for student in data:
            validate()
            assign()
        output()

    run()


school1 = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 73},
    {"name": "Charlie", "marks": 102},  # Invalid
    {"name": "Dave", "marks": 60}
]

school2 = [
    {"name": "Ronald", "marks": 80},
    {"name": "Johnson", "marks": 90},
    {"name": "Umar", "marks": 607},  # Invalid
    {"name": "Farooq", "marks": 75}
]

validate_and_mark(school1)
validate_and_mark(school2)