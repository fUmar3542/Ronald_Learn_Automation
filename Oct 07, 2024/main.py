# #######################################################################################
# Quiz Question: Grocery Bill Calculator with Predefined Prices
# #######################################################################################
# 	Objective:
# 		Create a Python program that calculates the total cost of items in a grocery list using pre-defined prices, applies a discount if applicable, and provides the final bill along with item-wise prices.
#
# 	Requirements:
#
# 	Product Price List:
# 		The program should have a pre-defined list of products and their respective prices.
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
# Enter the product name (or type 'done' to finish): Apples
# Enter the quantity of Apples: 3
# Enter the product name (or type 'done' to finish): Milk
# Enter the quantity of Milk: 2
# Enter the product name (or type 'done' to finish): Bananas
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
# Final Bill: $15.50
