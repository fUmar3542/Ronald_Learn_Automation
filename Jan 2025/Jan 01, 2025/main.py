# Matrix Manipulation
#
# Write a Python program to:
#
# 1) Accept a 3x3 matrix (list of lists) from the user.
# 2) Find the sum of each row and sum of each column.
# 3) Print the matrix, row sums, and column sums.
#
# Input:
#
# Enter elements of the 3x3 matrix row by row:
# 1 2 3
# 4 5 6
# 7 8 9
#
#
# Output:
#
# Matrix:
# 1 2 3
# 4 5 6
# 7 8 9
#
# Row Sums: [6, 15, 24]
# Column Sums: [12, 15, 18]

# 1) First solution

# # Section I. Variables
#
# check = False
# number_of_rows = 3
# number_of_columns = 3
# matrix = []
# sum_of_rows = []
# sum_of_columns = []
#
# # Section II. User Input
#
# for i in range(number_of_rows):
#     while True:
#         try:
#             user_input = list(map(int, input("Enter integers: ").split()))
#             check = True
#             matrix.append(user_input)
#             break
#         except:
#             print("Error: please enter a valid integer.")
#
# # Section III. Display
#
# print("")
# print("Matrix:")
#
# matrix_len = len(matrix)
#
# for i in range(matrix_len):
#     string_element = [str(i) for i in matrix[i]]
#     print(' '.join(string_element))
#
# # Section IV. Calculations
#
# for iteration in range(number_of_rows):
#     row_sum = 0
#     for count_1 in range(matrix_len):
#         row_sum = row_sum + matrix[iteration][count_1]
#     sum_of_rows.append(row_sum)
#
# print("")
# print(f"Sum of Rows: {sum_of_rows}")
#
# for iteration in range(number_of_columns):
#     column_sum = 0
#     for count_2 in range(matrix_len):
#         column_sum = column_sum + matrix[count_2][iteration]
#     sum_of_columns.append(column_sum)
# print(f"Sum of Columns: {sum_of_columns}")


#########################################################################

# 2nd solution

# Section I. Variables

check = False
number_of_rows = 3
number_of_columns = 3
matrix = []
sum_of_rows = []
sum_of_columns = []

# Section II. User Input

for i in range(number_of_rows):
    while True:
        try:
            user_input = list(map(int, input("Enter integers: ").split()))
            check = True
            matrix.append(user_input)
            break
        except:
            print("Error: please enter a valid integer.")

# Section III. Display

print("")
print("Matrix:")

matrix_len = len(matrix)

for i in range(matrix_len):
    string_element = list(map(str, matrix[i]))
    print(string_element)

# Section IV. Calculations

sum_of_rows = [sum(item) for item in matrix]

print("")
print(f"Sum of Rows: {sum_of_rows}")

for iteration in range(number_of_columns):
    column_sum = 0
    for count_2 in range(matrix_len):
        column_sum = column_sum + matrix[count_2][iteration]
    sum_of_columns.append(column_sum)
print(f"Sum of Columns: {sum_of_columns}")
