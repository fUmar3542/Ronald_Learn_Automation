

# 1) Solution to compare things according to our requirements

# string1 = "high"
# string2 = "low"
#
# number1 = 2
# number2 = 1
#
# if string1 == "low":
#     value1 = number2
# else:
#     value1 = number1
#
# if string2 == "low":
#     value2 = number2
# else:
#     value2 = number1
#
# print(value1)
# print(value2)
#
# if value1 > value2:
#     print("String1")
# else:
#     print("String2")
#
# # if string1 > string2:
# #     print("String1")
# # else:
# #     print("String2")



# 2)

# string1 = "high"
# string2 = "low"
#
# priority_number = ["low", "high"]
#
# if priority_number.index(string1) > priority_number.index(string2):
#     print("String1")
# else:
#     print("String2")


# 3)

string1 = "high"
string2 = "low"

priority_number = {"low": 1, "high": 2}

if priority_number[string1] > priority_number[string2]:
    print("String1")
else:
    print("String2")



