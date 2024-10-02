

# ##############################################################################################################
# # Problem: Advanced Inventory Price Checker with Category Filter
# # You are managing an inventory of products, each with a category, and you need to:
# #
# # Check if the prices exceed a given threshold, but only for products in a specific category.
# # print the product names and their prices if the price exceeds the threshold and the product is in the selected category.
# # Ensure the product names are title-cased in the result.


product_list = [
                ["computers", "Dell X450", 1200],
                ["shoes","Air Jordan's", 50],
                ["books", "War and Peace", 10],
                ["games", "Halo", 20],
                ["Computers", "Dell X400", 1000],
            ]

category_input = input("Please enter a product category: Shoes, Books, Games, or Computers: ")
price_threshold = float(input("Please enter your dollar budget: "))

# results = []
# for item in product_list:
#     if item[0].lower() == category_input.lower() and item[2] > price_threshold:
#         results.append(item)

results = []
for item1, item2, item3 in product_list:
    if item1.lower() == category_input.lower() and item3 > price_threshold:
        results.append([item1, item2, item3])

# results = []
# length = len(product_list)
# for i in range(length):
#     if product_list[i][0].lower() == category_input.lower() and product_list[i][2] > price_threshold:
#         results.append(product_list[i])


# lower_category_input = category_input.lower()
# valid_product_input = ["shoes", "books", "games", "computers"]
# length = len(lower_category_input)
# if lower_category_input in valid_product_input:
#
#     category_list = ["shoes", "books", "games", "computers"]
#     category_index = category_list.index(category_input)
#
#     if category_input == product_list[category_index][0]:
#         if price_threshold < product_list[category_index][2]:
#             print("You cannot afford: " + product_list[category_index][1] + " " + "Cost: $" + str(product_list[category_index][2]))
#         else:
#             print("You can afford the product")
