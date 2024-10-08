
#######################################################################################
# Quiz Question: Grocery Bill Calculator with Predefined Prices
# #######################################################################################
# 	Objective:
# 		Create a Python program that calculates the total cost of items in a grocery list using pre-defined prices,
# 		applies a discount if applicable, and provides the final bill along with item-wise prices.
#
# 	Requirements:
#
# 	Product Price List:
# 		The program should have a pre-defined list of products and their respective prices. [completed]
#
# 	User Input:
# 		Prompt the user to enter the number of items.
# 		Prompt the user to input the name of the items they purchased from the list.
# 		For each item, ask the user to input the quantity.
# 		Calculate the total bill by multiplying the quantity with the corresponding item’s price.
# 		If the user enters a product name that is not in the price list, notify them and ask for a valid product.
# 		If no items are entered, show an appropriate message.
# 	Apply a Discount:
#
# 		If the total bill exceeds $100, apply a 10% discount.
# 		Otherwise, no discount should be applied.
# 	Display:
#
# 		Show the original bill (before any discount).
# 		If a discount is applied, display the discount amount.
# 		Display the final amount after applying the discount.
# 		Ensure the final bill and each item's price are displayed with two decimal points.
# 		Display the total using string formatting.
#
#
# Example Expected Program Flow:
#
# Enter the number of items: 3
#
# Enter the product name: Apples
# Enter the quantity of Apples: 3
# Enter the product name: Milk
# Enter the quantity of Milk: 2
# Enter the product name: Bananas
# Enter the quantity of Bananas: 6
#
# Number of items purchased: 3
#
# Item-wise prices:
# Apples (x3.0): $4.50
# Milk (x2.0): $6.50
# Bananas (x6.0): $4.50
#
# Original Bill: $15.50
# Final Bill: $15.


###################################################################################
# Umar's solution

# product_list = [["apples", 3.00],
#                 ["pears", 2.00],
#                 ["peaches", 4.00],
#                 ["pizza", 10.00],
#                 ["milk", 5.00],
#                 ["crackers", 7.00],
#                 ["juice", 4.00],
#                 ["mango", 3.00],
#                 ["raisins", 4.00],
#                 ["cereal", 5.00]
#                 ]

product_list = [
    ["apple", "pear", "peach", "pizza", "milk","cracker", "juice", "mango", "raisin", "cereal"],
    [3.00, 2.00, 4.00, 10.00, 5.00, 7.00, 4.00, 3.00, 4.00, 5.00]
]

try:
    number_of_items_input = int(input("Enter the number of items: "))
except:
    print("Enter a valid number")
else:
    check = False
    product_name = input("Enter product name: ")
    if product_name.lower() in product_list[0]:
        check = True
        quantity = input("Enter quantity: ")
    else:
        print("Product not found")
        product_name = input("Enter product name: ")
        if product_name.lower() in product_list[0]:
            check = True
            quantity = input("Enter quantity: ")

    # quantity = input("Enter quantity: ")

    # found = False
    # for i in range(len(product_list)):
    #     if product_name.lower() == product_list[i][0]:
    #         found = True
    # if found:
    #     quantity = input("Enter quantity: ")


############################################################################################################
# Ronald's program


# Product list and prices

# product_list = [["apples", 3.00],
#                 ["pears", 2.00],
#                 ["peaches", 4.00],
#                 ["pizza", 10.00],
#                 ["milk", 5.00],
#                 ["crackers", 7.00],
#                 ["juice", 4.00],
#                 ["mango", 3.00],
#                 ["raisins", 4.00],
#                 ["cereal", 5.00]
#                 ]
#
# single_product_list = ["apple", "pear", "peach", "pizza", "milk",
#                        "cracker", "juice", "mango", "raisin", "cereal"]
#
# single_price_list = [3.00, 2.00, 4.00, 10.00, 5.00, 7.00, 4.00, 3.00, 4.00, 5.00]
#
# # product_list = [
# #     ["apple", "pear", "peach", "pizza", "milk","cracker", "juice", "mango", "raisin", "cereal"],
# #     [3.00, 2.00, 4.00, 10.00, 5.00, 7.00, 4.00, 3.00, 4.00, 5.00]
# # ]
#
# # User enters input
# # Prompt the user to enter the number of items. [completed]
# # Prompt the user to input the name of the items they purchased from the list. [completed]
# # For each item, ask the user to input the quantity. [completed]
# # populate invalid message if the entered item is not in the product list [completed]
# # Calculate the total bill by multiplying the quantity with the corresponding item’s price [in progress].
#
#
# total_list = []
# for_loop_count = 0
#
# try:
#     number_of_items_input = int(input("Enter the number of items: "))
# except:
#     print("Enter a valid number")
# else:
#     while for_loop_count != number_of_items_input:
#         try:
#             product_name_input = input("Enter the product name: ").lower()
#             quantity_input = int(input(f"Enter the quantity of {product_name_input}: "))
#         except:
#             print("Please enter a valid name or quantity")
#
#         if product_name_input in single_product_list:
#             single_product_index = single_product_list.index(product_name_input)
#             quantity_input = input(f"Enter the quantity of {product_name_input}: ")
#             if quantity_input is quantity_input.isnumeric():
#                 total_list.append(product_name_input)
#                 for_loop_count = for_loop_count + 1
#         else:
#             print("Enter a valid quantity")
