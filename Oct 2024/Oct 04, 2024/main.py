
#############################################################
# F Notation

# name = "Umar"
# ssn = 1234567
#
# # My name is Umar and my ssn number is 1234567.
#
# print("My name is " + name + " and my ssn number is " + str(ssn))
#
# print("My name is", name, "and my ssn number is", ssn)
#
# print(f"My name is {name} and my ssn number is {ssn}")
#
# # print(name)



#############################################################
# Insert vs replace

# name = "Umar farooq"
#
# print(name.replace('a', "F"))

# Insert

# names_list = ["Umar", "Farooq", "Ronald","Johnson"]
# name = "James"
#
# # Append elemnt to the end
# # names_list.append("James")
#
# # Join 2 lists
# # other_list = ['1']
#
# # other_names = [name]
# #
# # third_list = names_list + [name]
# #
# # third_list.extend(other_names)
# #
# # for x in other_names:
# #     third_list.append(x)
# #
# # print(third_list)
#
#
# # # Slicing
# # names_list = names_list[:2] + [name] + names_list[2:]
# # names_list = names_list[:3] + [name] + names_list[3:]
# #
# # print(names_list)
#
# other_list = [1,2,3,4,5]
#
# # Isnert
# for i in range(len(other_list)):
#     names_list.insert(2+i, other_list[i])
#
# names_list.insert(2, other_list[0])
# names_list.insert(3, other_list[1])
# names_list.insert(4, other_list[2])
# names_list.insert(5, other_list[3])
# names_list.insert(6, other_list[4])
#
# print(names_list)
#
# names_list = names_list[:2] + other_list + names_list[2:]
#
# # names_list.insert(2, [other_list])



#############################################################
# Enumerate


name = "Umar Farooq"

# 0 U
# 1 m

# i = -1
# for item in name:
#     i = i + 1
#     print(i, item)

print(enumerate(name))

# 0 -> U

# [('0': 'U'), ('1': 'm'), ...}

for count, item in enumerate(name):
    print(count, item)
