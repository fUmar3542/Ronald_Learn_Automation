import array

######################################################################################################

# Sort Lists

numbers_list = [34, 32, 12, 56, 45]

# numbers_list.sort()
#
# print(numbers_list)

# Perform some arithematic operation on each element before performing the operation of sorting


def do_arithematic(number):
    return number - 100


# numbers_list.sort(key=do_arithematic)
# print(numbers_list)


# names_list = ["Umar", "Ronald", "James", "Jole", "Lee", "abdullah"]
# # names_list.sort()
# # print(names_list)
#
# # Ascending
# names_list.sort(key=str.lower)
# print(names_list)
#
# # Descending
# names_list.reverse()
# print(names_list)
#
# # Descending
# names_list.sort(reverse=True)
# print(names_list)


######################################################################################################

# Copy Lists

numbers_list = [34, 32, 12, 56, 45]

# Copying of the address of the numbers list to resultant list
# resultant_list = numbers_list

# numbers_list[0] = 100
#
# print(resultant_list)


# 1) copy method
# resultant_list = numbers_list.copy()

# numbers_list[0] = 100
#
# print(numbers_list)
# print(resultant_list)


# 2) slicing
resultant_list = numbers_list[:]

# numbers_list[0] = 100
#
# print(resultant_list)

# 3) loop
# resultant_list = []
# for x in numbers_list:
#     resultant_list.append(x)

######################################################################################################

# Join Lists

# 1) +
sum_list = numbers_list + resultant_list
print(sum_list)

# 2) extend
numbers_list.extend(resultant_list)
sum_list = numbers_list[:]
print(sum_list)

######################################################################################################

# Escape sequences

# \n -> new line

print("Ronald\nJohnson")

# \t

print("Ronald\tJohnson")


######################################################################################################

# find

name = "Ronald Johnson"

# print(name.find("on"))
#
# # rfind -> reverse
#
# print(name.rfind("on"))
#
# # index / rindex
#
# print(name.index("on"))
#
# print(name.rindex("on"))


# print(name.find("Umar"))      # -1

# print(name.index("Umar"))     # Error


######################################################################################################

student_list = [12, "Ronald Johnson", "ronald@gmail.com", "address"]
print(student_list)


numbers_array = array.array("i", [1,2,3,4,5,5])
print(numbers_array)


pin_list = [615, 7162, 1827, 216]

pin = int(input("Enter new pin: "))
pin_list[0] = pin


resultant_list = []
for x in numbers_list:
    resultant_list.append(x * 5)

