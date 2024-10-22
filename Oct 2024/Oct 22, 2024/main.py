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
    [3.00, 2.00, 4.00, 10.00, 5.00, 7.00, 4.00, 3.50, 4.00, 5.00]
]

# Getting input from user
count = 1000
check = False
quantity = 1
number_of_items_input = 0
for i in range(count):
    try:
        number_of_items_input = int(input("Enter the number of items: "))
        if number_of_items_input > 0:
            check = True
            break
    except:
        print("Enter a valid number.")

user_inputs = [[], []]
result_list = []
bill_result = 0
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
            product_index = product_list[0].index(product_name)
            price = product_list[1][product_index]
            total_price = user_inputs[1][item] * price
            bill_result = bill_result + total_price
            result_list.append(total_price)
            print("-------------------------------------------------------")

# Display output
print(f"Number of items purchased: {number_of_items_input}")
print("")
print("Item-wise prices: ")

print("")

for i in range(number_of_items_input):
    print(f"{(user_inputs[0][i]).capitalize()} (x{user_inputs[1][i]}): ${result_list[i]:.2f}")

print(f"Original Bill: ${float(bill_result):.2f}")

if bill_result > 100:
    discount = bill_result * 0.90
    print(f"Final Bill: ${discount:.2f}")
else:
    print(f"Final Bill: ${bill_result:.2f}")

