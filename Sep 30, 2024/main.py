# Problem: Sentence Case Formatter
# You are given a list of sentences with inconsistent case formatting. Your task is to ensure that:
#
# Each sentence starts with a capital letter.
# The rest of the sentence should be in lowercase.
# Sentences should end with either a period (.), exclamation mark (!), or question mark (?). Please only print the valid output.

sentences = ["PEACE and war is a good book#",
             "you should read crime AND PUNISHMENT book",
             "atomic HABITS is written by James$"
            "bekjbkje 3827498 wkfw$jwebjk#",
             "kebdkjk",
             "1238929372 9847989",
             "###############"
             "A tale of a river is a column.",]

special_characters = ['.', '!', '?']
count = 0

for sentence in sentences:
    lower_sentence = sentence.lower()
    length = len(lower_sentence)
    if lower_sentence and not lower_sentence.isspace() and not lower_sentence.isnumeric():            # if len(sentence) > 0:
        if lower_sentence[-1] not in special_characters:
            lower_sentence = lower_sentence[0].capitalize() + lower_sentence[1:] + "."
            print(lower_sentence)
        else:
            lower_sentence = lower_sentence[0].capitalize() + lower_sentence[1:]
            print(lower_sentence)
    # else:
    #     print("Invalid character used in sentence: " + sentence[count])



# ##############################################################################################################
#
# # Problem : Advanced Email Domain Extractor with Subdomains
# # You are given a list of email addresses, and your task is to:
# #
# # Extract the domain from each email address.
# # Ensure all domains are in lowercase.
# # Separate the main domain from subdomains (e.g., for john@sub.example.com, extract example.com).
# # print a list of unique main domains.
#
# email_list = ["michaeljackson@yahoo.com",
#               "tonystark@aol.com",
#               "bobsmith@aol.com",
#               "michaeljordan@OUTLOOK.com",
#               "sashafierce@sub.UK.org"]
#
# domain_list = []
#
# for email in email_list:
#     period_count = email.count(".")
#     if period_count > 1:
#         period_index = email.find(".")
#         domain1 = email.lower()[period_index + 1:]
#         domain_list.append(domain1)
#     else:
#         indices = email.rfind("@")
#         domain2 = email.lower()[indices + 1:]
#         print(domain2)
#         domain_list.append(domain2)
#
# print(set(domain_list))
#
#
# ##############################################################################################################
#
#
# # Problem: Advanced Inventory Price Checker with Category Filter
# # You are managing an inventory of products, each with a category, and you need to:
# #
# # Check if the prices exceed a given threshold, but only for products in a specific category.
# # print the product names and their prices if the price exceeds the threshold and the product is in the selected category.
# # Ensure the product names are title-cased in the result.
#
# category_input = input("Please enter a product category: Shoes, Books, Games, or Computers: ".capitalize())
# price_threshold = float(input("Please enter your price threshold: "))
# product_list = [
#                 ["Shoes","Air Jordan's", 50],
#                 ["Books", "War and Peace", 10],
#                 ["Games", "Halo", 20],
#                 ["Computers", "Dell X400", 1000]
#                 ]
#
# if category_input == product_list[0][0]:
#     if price_threshold < product_list[0][2]:
#         print(product_list[0][1] + " " + str(product_list[0][2]))
#
# elif category_input == product_list[1][0]:
#     if price_threshold < product_list[1][2]:
#         print(product_list[1][1] + " " + str(product_list[1][2]))
#
# elif category_input == product_list[2][0]:
#     if price_threshold < product_list[2][2]:
#         print(product_list[2][1] + " " + str(product_list[2][2]))
#
# elif category_input == product_list[3][0]:
#     if price_threshold < product_list[3][2]:
#         print(product_list[3][1] + " " + str(product_list[3][2]))
#
# else:
#     print("Invalid category")
#
