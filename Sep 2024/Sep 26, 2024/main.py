

books = ["PEACE and war", "crime AND PUNISHMENT", "atomic HABITS and", "A tale of a river"]
# books = ["A tale of a river a"]
prepositions = ["a", "an", "the", "and", "in", "of", "to"]

for book_title in books:
    words = book_title.lower().split()
    print("---------------")
    print(words)
    length = len(words)
    for count, word in enumerate(words):
        if (word not in prepositions) or (count == 0) or (count == (length -1)):
            words[count] = word.capitalize()
    print(words)
    # String to list
    result = ""
    for word in words:
        result = result + " " + word





################################################################


# books = ["PEACE and war", "crime AND PUNISHMENT", "atomic HABITS and", "A tale of a river"]
# # books = ["A tale of a river a"]
# prepositions = ["a", "an", "the", "and", "in", "of", "to"]
#
# # books[0] = "123"
#
# for book_title in books:
#     # print(type(book_title))
#     words = book_title.lower().split()
#     # print(type(words))
#     print( "---------------")
#     print(words)
#     temp_list = []
#     length = len(words)
#
#     for count, word in enumerate(words):
#         # if word not in prepositions:
#         #     temp_list.append(word.capitalize())
#         # elif count == 0 or count == (len(words) - 1):
#         #     temp_list.append(word.capitalize())
#         # else:
#         #     temp_list.append(word)
#
#         if (word not in prepositions) or (count == 0) or (count == (length -1)):
#             temp_list.append(word.capitalize())
#         else:
#             temp_list.append(word)
#
#     # for word in words:
#     #     if word not in prepositions:
#     #         a = word.capitalize()
#     #         temp_list.append(a)
#     #     elif word == words[0] or word == words[-1]:
#     #         a = word.capitalize()
#     #         temp_list.append(a)
#     #
#     #         for count, word in enumerate(words):
#     #             if word in prepositions and count != 0 and count != len(words) - 1:
#     #                 b = word.lower()
#     #                 temp_list.append(b)
#     #             else:
#     #                 temp_list.append(word)
#
#     print(temp_list)
