#
#
# #########################################################################
#
# # 2nd solution
#
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
#     string_element = list(map(str, matrix[i]))
#     print(' '.join(string_element))
#
# # Section IV. Calculations
#
# sum_of_rows = [sum(item) for item in matrix]
#
# print("")
# print(f"Sum of Rows: {sum_of_rows}")
#
# sum_of_columns = [sum(matrix[j][i] for j in range(number_of_columns)) for i in range(number_of_rows)]
#
# print(f"Sum of Columns: {sum_of_columns}")


##################################################################################

# Dictionary

# Hash tables
# Key value pairs

names = {"Ronald", "Umar"}

student1 = [123, "Ronald Johnson", "ronald.johnson@gmail.com"]
student2 = ["Umar Farooq", 124, "umar.farooq@gmail.com"]

print(student1[0], student2[0])

student1_dict = {
    "id": {"id1": 23},
    "email": "ronald.johnson@gmail.com",
    "name": ["Ronald Johnson", "Umar Farooq"],
}

# a = [1, 2]
# a = 1
# print(a)

# Access the values

# print(student1_dict.get("name"))
print(student1_dict["name"])

# Add some specific element

# student1_dict['year'] = 2019

student1_dict.update({"year": 2019})

print(student1_dict)


# Update some specific element

student1_dict['year'] = 2019

student1_dict.update({"year": 2019})

print(student1_dict)







