
FILE_PATH = "/Volumes/D/Projects/Pycharm/Outwork/Ronald_Learn_Automation/Aug 2025/Aug 28, 2025/test.txt"

# File Handling

# Text File

# open -> Built-in function to open the file

# Operations:
# r -> read
# w -> write
# a -> append
# x -> create

# 1)
file = open(FILE_PATH, "r")
content = file.read()
file.close()

# print(content)

# 2)

with open(FILE_PATH, "r") as file:
    content = file.read()
    # print(type(content))
    # print(content)


# # Write
#
# # 1)
# with open(FILE_PATH, "w") as file:
#     file.write("data7, data8")
#
#
# with open(FILE_PATH, "r") as file:
#     content = file.read()
#     print(content)

# Write

student = [
    "Ronald, 1, USA\n",
    "Johnson, 2, USA\n",
]

# 1)
with open(FILE_PATH, "a") as file:
    file.write("data7, data8" + "\n")


with open(FILE_PATH, "r") as file:
    content = file.read()
    # print(content)

with open(FILE_PATH, "a") as file:
    file.writelines(student)


with open(FILE_PATH, "r") as file:
    index = 1
    for line in file:
        print(f"Line No: {index} - {line}")
        index += 1




# JSON

# key value pair

student_list = [
    {
        "Name": "Ronald",
        "Roll Number": 1
    },
    {
        "Name": "Johson",
        "Roll Number": 2
    },
]

import json

# write

with open("json_file.json", "w") as file:
    json.dump(student_list, file)

# read

with open("json_file.json", "r") as file:
    content = json.load(file)
    print(content)

