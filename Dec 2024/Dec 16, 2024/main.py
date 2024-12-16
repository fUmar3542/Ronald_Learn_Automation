
# Constant
# const int a = 12

# Lists -> changeable, ordered

# Tuple -> unchangeable, ordered
names_tuple = ("Ronald", "Umar", "Ronald", "Umar", "Ronald", "Umar")
names1_tuple = ("Ronald", "Umar")

# names_tuple = (names1_tuple, "Joe")
#
# print(names_tuple)

# # Access elements
# print(names_tuple[1:5])

# # Display elements
# for i in range(len(names_tuple)):
#     print(names_tuple[i])
#
# for x in names_tuple:
#     print(x)


# Update tuple elements

# Add elements to tuple

element = []
for x in names_tuple:
    element.append(x)
element.append("Joe")

# list = list1 + list2

# # First solution
# names_tuple = names_tuple + ("Joe",)
# print(names_tuple)

# Second solution

# Wrong
# s = str(names_tuple) + "Joe"
# print((s,))

# s = "123"
# print(int(s)/10)

# Correct
print(type(names_tuple))
names_list = list(names_tuple)
names_list.append("Joe")

print(names_list)

names_tuple = tuple(names_list)

print(names_tuple)


currency_values = (
    # 0: EUR: 1:GBP, 2:JPY, 3:PKR, 4:PESO, 5:USD
    [1, 0.954, 0.783, 150.527, 275, 58.01], # EUR
    [0.954, 1, 0.783, 150.527, 275, 58.01], # GBP
    [1.5, 4.54, 1, 485, 38.4, 75], # JPY
    [94.3, 85.4, 473, 1, 74.3, 45.5], # PKR
    [14.75, 15.27, 275.81, 1, 58.12], # Peso
    [1.5, 4.54, 485, 38.4, 75, 1], # USD
)


names_list = ['Umar', 'Ronald']

# Wrong
# names_tuple = names1_tuple + names_list


# Unpacking of tuples

names1_tuple = ("Ronald", "Umar", "Ronald")

# name1 = names1_tuple[0]
# name2 = names1_tuple[1]

(name1, *name2) = names1_tuple

print(name1)
print(name2)


#############################################################
# Set


