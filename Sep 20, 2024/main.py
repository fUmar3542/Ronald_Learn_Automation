

# 1) Create a program which will remove the specific elements from the list.
# like if we have a list of 4 numbers lik [1,2,3,1]. and if we'll be running the program
# to remove 1 from the list it should print [2,3] on console.

# user_input = list(map(int,input("Enter a list of four integers: ").split()))
# print("Entered list: " + str(user_input))
# remove_int = int(input("Enter an integer to be removed from the list: "))
# remove_string = str(remove_int)
# print("You have selected " + str(remove_int) + " as the integer to remove from the list")
# print("")
#
# user_input = str(user_input)
#
# print(type(user_input))
#
# updated_list = user_input.replace(remove_string, "")
#
# new_list = updated_list.split(',')
#
# print(updated_list)
# print(new_list)


# numbers = [1,2,3,4,5,1]
# key = 1
# resultant = []
#
# print(numbers.index(key))
#
# print(numbers.count(key))


##############################################

# Loops

# go through the collection of data -> lists, tuple, sets, user defined data.


# For Loop

# Simple for loop with range keyword

# loops

# initialization -> only once
# comparison        -> on each iteration
# incremented assignment -> i = i + 1  -> on each iteration
# breakage

# i = i + (-2)

numbers = [1,12,3,84,5, 7, 1, 1, 8, 5]
key = 1

length = len(numbers)

# for i in range(0, length):
#     if numbers[i] == key:
#         numbers.remove(key)
#     print(numbers[i])

# resultant = []
# for i in range(0, length):
#     if numbers[i] != key:
#         resultant.append(numbers[i])
#
# print(resultant)


count = numbers.count(key)
for i in range(0, count):
    numbers.remove(key)


# Foreach loop


# While loop
