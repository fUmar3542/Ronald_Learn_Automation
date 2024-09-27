
##########################################################################################

# books = ["PEACE and war", "crime AND PUNISHMENT", "atomic HABITS and", "A tale of a river"]
# # books = ["A tale of a river a"]
# prepositions = ["a", "an", "the", "and", "in", "of", "to"]
#
# for book_title in books:
#     words = book_title.lower().split()
#     length = len(words)
#     for count, word in enumerate(words):
#         if (word not in prepositions) or (count == 0) or (count == (length -1)):
#             words[count] = word.capitalize()
#
#     # List to String
#
#     # Built-in function
#     result = ' '.join(words)
#     print(result)
#
#
#     # Code from scratch
#     # result = ""
#     # for word in words:
#     #     result = result + " " + word
#     # result = result.strip()
#     # # result = result[1:]
#     # print(result)



###############################################################
# Problem: Sentence Case Formatter
# You are given a list of sentences with inconsistent case formatting. Your task is to ensure that:
#
# Each sentence starts with a capital letter.
# The rest of the sentence should be in lowercase.
# Sentences can end with either a period (.), exclamation mark (!), or question mark (?).

sentences = ["PEACE and war is a good book",
             "you should read crime AND PUNISHMENT book",
             "atomic HABITS is written by James",
             "A tale of a river is a column."]

characters = ['.', '!', '?']

for sentence in sentences:
    # lower_sentence = sentence.lower().split()
    # lower_sentence[0] = lower_sentence[0].capitalize()
    # # print(lower_sentence)
    #
    # print(' '.join(lower_sentence))

    lower_sentence = sentence.lower()
    lower_sentence = lower_sentence[0].capitalize() + lower_sentence[1:]
    print(lower_sentence)



# lower_sentence = ["jsdj", "jdwbjw", "dbjkew"]
# lower_sentence[0] = lower_sentence[0].capitalize()



#########################################################

# Problem : Advanced Email Domain Extractor with Subdomains
# You are given a list of email addresses, and your task is to:
#
# Extract the domain from each email address.
# Ensure all domains are in lowercase.
# Separate the main domain from subdomains (e.g., for john@sub.example.com, extract example.com).
# print a list of unique main domains.


#########################################################
#
# Problem: Advanced Inventory Price Checker with Category Filter
# You are managing an inventory of products, each with a category, and you need to:
#
# Check if the prices exceed a given threshold, but only for products in a specific category.
# print the product names and their prices if the price exceeds the threshold and the product is in the selected category.
# Ensure the product names are title-cased in the result.
