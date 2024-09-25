

# numbers = [1, 3, 5, 65]
# for count, item in enumerate(numbers):
#     if count != 1:
#         print(item)

# Practice Question # 2
# You are given a list of book titles with inconsistent formatting.
# Your goal is to clean up these titles by ensuring that:
#
# The first letter of each word should be in a capitalized format.
# The remaining letters of each word are lowercase.
# Words like "a", "an", "the", "and", "in", "of", and "to" should remain
# lowercase unless they are the first or last word in the title.   (Hint: built in functions)

# Title
# TITLE

# Solution

# When we'll be calling the len() function on a list -> It'll be giving us the number of elements present in that specific list
# When we'll be calling the len() function on a string -> It'll be giving us the number of characters present in that specific string
# prepositions.index(word) == -1
# AND != and

books = ["and war AND PEACE and", "crime AND PUNISHMENT", "atomic HABITS"]
prepositions = ["a", "an", "the", "and", "in", "of", "to"]

for book_title in books:
    # print(type(book_title))
    words = book_title.lower().split()
    # print(type(words))
    print( "---------------")
    print(words)
    temp_list = []
    for word in words:
        if word not in prepositions:
            a = word.capitalize()
            temp_list.append(a)
        elif word == words[0] or word == words[-1]:
            a = word.capitalize()
            temp_list.append(a)
        else:
            temp_list.append(word)
    print(temp_list)

