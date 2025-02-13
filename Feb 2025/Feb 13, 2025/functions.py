import random


# Write a program which will be getting the name and id of the student. write a function for that.
# Do some exception handling. This function will also return the id and name of the student.
# we'll be creating a validity_check function which will return True in case if the id is between
# 1 and 100 and name is present in our list, otherwise return False.

name_list = ["Ronald", "Michael", "James", "Sally"]


def get_user_input():
    while True:
        check = False
        name = input("Enter name: ").lower().strip()
        name = name.capitalize()
        if name and not name.isnumeric():
            check = True
            break
        else:
            print("Error: entry must not be empty and contain only alphabetic characters.")
    if check:
        while True:
            try:
                student_id = int(input("Enter student id: "))
                break
            except:
                print("Error: please enter only integers for the student id. Please try again")
    return name, student_id


def validity_check(name1, student_id1):
    if name1 in name_list and 0 < student_id1 < 100:
        return True
    return False



name, student_id = get_user_input()
validity_check(student_id1=student_id, name1=name)
print("Program complete.")



