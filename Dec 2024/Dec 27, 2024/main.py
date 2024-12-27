
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

# Section I. Variables

check = False
number_of_rows = 3

# int_user_input_1 = []
# int_user_input_2 = []
# int_user_input_3 = []

matrix = []

index_0_to_string = []
index_1_to_string = []
index_2_to_string = []

# matrix = []

# Section II. User Input

# 1) Optimize the solution w.r.t to space
# 2) Modify the solution w.r.t the formatting provided in the problem statment

for i in range(number_of_rows):
    while True:
        try:
            int_user_input_1 = []
            user_input_1 = input("Enter three integers: ")
            split_user_input_1 = user_input_1.split()
            for i in split_user_input_1:
                i = int(i)
                int_user_input_1.append(i)
            check = True
            matrix.append(int_user_input_1)
            break
        except:
            print("Error: please enter a valid integer.")

# if check:
#
#     while True:
#         try:
#             user_input_2 = input("Enter three integers: ")
#             split_user_input_2 = user_input_2.split()
#             for i in split_user_input_2:
#                 i = int(i)
#                 int_user_input_2.append(i)
#             check = True
#             break
#         except:
#             print("Error: please enter a valid integer.")
#
#     if check:
#
#         while True:
#             try:
#                 user_input_3 = input("Enter three integers: ")
#                 split_user_input_3 = user_input_3.split()
#                 for i in split_user_input_3:
#                     i = int(i)
#                     int_user_input_3.append(i)
#                 check = True
#                 break
#             except:
#                 print("Error: please enter a valid integer.")

# Section III. Display

print("")
print("Matrix:")
# matrix = [int_user_input_1,
#           int_user_input_2,
#           int_user_input_3]

matrix_len = len(matrix)
j = 0

# 1 2 3
# 4 5 6
# 7 8 9

# 3) We have to write a dynamic solution to convert the elements from int to strings

while j != matrix_len:
    j = j
    for i in range(matrix_len):
        element = matrix[j][i]
        string_element = str(element)
        if j == 0:
            index_0_to_string.append(string_element)
        elif j == 1:
            index_1_to_string.append(string_element)
        elif j == 2:
            index_2_to_string.append(string_element)
    j = j + 1

print(' '.join(index_0_to_string))
print(' '.join(index_1_to_string))
print(' '.join(index_2_to_string))

# Section IV. Calculations

sum_of_rows = []
sum_of_columns = []
count_1 = 0
count_2 = 0
count_3 = 0

# Calculations
row_sum = 0
column_sum = 0
row_temp = 0
column_temp = 0

while row_temp != matrix_len:
    row_sum = 0
    for count_1 in range(matrix_len):
        row_sum = row_sum + matrix[row_temp][count_1]
    row_temp = row_temp + 1
    sum_of_rows.append(row_sum)

print(f"Sum of Rows: {sum_of_rows}")

while column_temp != matrix_len:
    column_sum = 0
    for count_2 in range(matrix_len):
        column_sum = column_sum + matrix[count_2][column_temp]
    column_temp = column_temp + 1
    sum_of_columns.append(column_sum)
print(f"Sum of Columns: {sum_of_columns}")



# sum = 0
# var1 = 12
# var2 = 10
#
# sum = sum + var1 + var2
#
# print(sum)
#
# sum = 0
# var3 = 10
# var4 = 14
#
# sum = sum + var3 + var4
#
# print(sum)


