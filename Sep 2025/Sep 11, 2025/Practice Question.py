#
# def view_all_students():
#     pass
#
#
# def get_user_input_value():
#     user_choice = 0
#     return user_choice
#
#
# def main():
#     while True:
#         user_choice = get_user_input_value()
#         print(user_choice)
#         if user_choice == 6:
#             break
#         if user_choice == 2:
#             view_all_students()
#
#
# main()



student_data = [["101", "Ronald Johnson", "34", "A"], ["102", "Michael Jordan", "62", "B"]]



# # Write Students Function

def write_students(student_data):
    with open("students.txt", "w") as file:
        for line in student_data:
            line_to_string = ", ".join(line) + "\n"
            file.write(line_to_string)

write_students(student_data)