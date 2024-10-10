
#####################################################
# Practice Question

# numbers = [12, 23, 9, 43, 12, 65, 67, 100, 87, 54, 25]
#
# # Write a program to find the largest and smallest from the list and print them in the end of program.
#
# largest_number = numbers[0]
# smallest_number = numbers[0]
#
# for number in numbers:
#     if number > largest_number:
#         largest_number = number
#     if number < smallest_number:
#         smallest_number = number
#
# print("Largest number: " + str(largest_number))
# print("Smallest number: " + str(smallest_number))



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
# Apples (x3): $4.50
# Milk (x2): $6.50
# Bananas (x6): $4.50
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
    print("Enter a valid number.")
else:
    user_inputs = [[], []]
    for item in range(number_of_items_input):
        product_name = ""
        quantity = 1
        check = False
        count = 1000
        for i in range(count):
            product_name = (input("Enter the product name: ")).lower()
            if product_name in product_list[0]:
                check = True
                break
            else:
                print("Product not found")
        if check:
            count = 1000
            check = False
            for i in range(count):
                quantity = input(f"Enter the quantity of {product_name}: ")
                if quantity.isnumeric() and int(quantity) > 0:
                    check = True
                    break
                else:
                    print("Invalid quantity")
            if check:
                user_inputs[0].append(product_name)
                user_inputs[1].append(int(quantity))
                print("-------------------------------------------------------")

# product_list = [
#     ["apple", "pear", "peach", "pizza", "milk","cracker", "juice", "mango", "raisin", "cereal"],
#     [3.00, 2.00, 4.00, 10.00, 5.00, 7.00, 4.00, 3.00, 4.00, 5.00]
# ]

#     print(product_list[0][7])
#     print(product_list[1][7])

    # Calculations
    final_result = [[], []]
    product_list_indexes = []
    for name in user_inputs[0]:
        product_index = product_list[0].index(name)
        product_list_indexes.append(product_index)

    print(product_list_indexes)



