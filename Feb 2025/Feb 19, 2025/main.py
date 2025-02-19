username = "175qwdjw"   # Global variable

#################################################################################################

# Arbitrary arguments/parameters
# *, **
# *args, **kwargs


# Whenever we are working with a combination of arguments/parameters,
# we should specify the simple variables first like without * or **
# and then we'll be specifying the parameters with * and at the end
# we'll be specifying the **kwargs.

def find_avg_and_display(student_name, *numbers):
    print(f"Student Name: {student_name}")
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")


# find_avg_and_display("Ronald", 96, 89, 78, 99, 88)


# **kwargs

# key-value pair

# def print_dict(**info):
#
#     # for item in info:
#     #     print(info[item])
#     #
#     # print(info.keys())
#     # print(info.values())
#     # print(info.items())
#
#     for key, value in info.items():
#         print(f"{key}: {value}")
#
#     # print(name)
#     # print(roll_number)
#     # print(address)
#     # print(email)
#     # print(marks)


# print_dict(name="Ronald", roll_number=12, address="USA", email="r@gmail.com", phone="+1236736281726", marks=[1,2,3,4,5])



###############################################################################################################

# Nested function

# Function within a function


def find_average():
    print()


def print_dict(**info):
    # global username
    username = "jwegfu828"
    print(username)
    count = 0

    def display_key_values():
        for key, value in info.items():
            print(f"{key}: {value}")

    def display_marks():
        for i in info["marks"]:
            print(i)




# print(count)                # Local variable
# display_key_values()
# display_marks()

print(username)
print_dict(name="Ronald", roll_number=12, address="USA", email="r@gmail.com", phone="+1236736281726", marks=[1,2,3,4,5])
print(username)


# number = 12
# number = 16
