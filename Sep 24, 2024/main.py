

# Problem
# Write a robust program to print all the items of a list on console
# without the second item using simple for loop and foreach loop as well.

# Simple For loop solution

# user_input = list(map(str,input("Enter in a list of items followed by spaces: ").split()))
# length = len(user_input)
#
# if length != 0:
#     print(user_input[0])
#
#     for n in range(2, length):
#         print(user_input[n])
#
#     # Foreach loop solution
#     user_input2 = list(map(str,input("Enter in a list of items followed by spaces: ").split()))
#
#     print(user_input2[0])
#     user_input2 = user_input2[2:]
#
#     for n in user_input2:
#         print(n)


numbers = [12, 43, 23, 45, 65, 43]
length = len(numbers)

# Simple for loop

# for i in range(0, length):
#     if i != 1:
#         print(numbers[i])

print("------------------------------------")

# Foreach loop

# check = True
# if length > 2:
#     second_item = numbers[1]
#     for item in numbers:
#         if item != second_item:
#             print(item)
#         else:
#             if not check:
#                 print(item)
#             check = False
# elif length != 0:
#     print(numbers[0])

numbers = []
empty_string = ""
count = 0
for item in numbers:
    if count != 1:
        print(item)
    count = count + 1

if numbers:             # if numbers is containing items | if len(numbers) > 0 | numbers != []
    print("Data.")

if empty_string:        # if empty_string is containing items | if len(empty_string) > 0 | if empty_string != ""
    print("Not an empty string")



# Practice Question # 2
# You are given a list of book titles with inconsistent formatting.
# Your goal is to clean up these titles by ensuring that:
#
# The first letter of each word is capitalized.
# The remaining letters of each word are lowercase.
# Words like "a", "an", "the", "and", "in", "of", and "to" should remain
# lowercase unless they are the first or last word in the title.   (Hint: built in functions)


# book_list = list(map(str,input("Enter in a list of books: ").split(',')))
# title_list = []
# single_word_list = []
#
# # It is a string within a list and not a list within a list.
#
# for book_title in book_list:
#     element = book_title.split()
#     title_list.append(element)
#
# # print(title_list)
#
# for list_element in title_list:
#     for word_element in list_element:
#         single_word_list.append(word_element)
#
# # print(single_word_list)
#
# for c in single_word_list:
#     capitalize = c.capitalize()
#     print(capitalize)
