
# List

# Access List Items
# Change List Items

# -------------------------------------------------
# Add List Items

# append, insert, extend

# numbers = [1,2,3,4,5]
# numbers1 = [1,26,7,8,9]
#
# # numbers.append(6)
# # numbers.append(7)
# # numbers.append(8)
# # numbers.append(9)
#
# # numbers U numbers1
# # numbers = [1,2,3,4,5,6,7,8,9]
#
# # 1)
# # numbers = numbers + numbers1
#
# # 2)
# numbers.extend(numbers1)
#
# tuple_of_numbers = (34,43,54)
#
# numbers.extend(tuple_of_numbers)
#
# print(numbers)

# -------------------------------------------------
# Remove List Items

# 1) remove

numbers = [10,1,2,3,10,5,6,"banana"]

# print(numbers.index(10))

# list.remove(value)  -> left to right
# numbers.remove("banana")

# 2.remove(2)
# numbers[-1].remove(2)  -> Incorrect -> performing remove function on an integer


# 2) pop -> [1,2,3,4] ->

# 4
# 3
# 2
# 1

# numbers.pop(-1)
# numbers.pop(4)

# numbers.remove(numbers[4])

# 3) del

# del numbers[4]
del numbers[0:2]
# del numbers


# 4) clear

numbers.clear()


print(numbers)


# ------------------------------------------------
# Practice Question

# 1) Create a program which will remove the specific elements from the list.
# like if we have a list of 4 numbers lik [1,2,3,1]. and if we'll be running the program
# to remove 1 from the list it should print [2,3] on console.


# 2) Shopping Cart Price Check
# You are creating a shopping cart system where users can add items to their cart.
# Each item has a price, and you need to calculate the total price based on certain conditions.
#
# Task:
# Create a list called cart that contains the following items and
# their prices: ["Apple", "Banana", "Orange", "Mango"] and corresponding prices Apple = $1.50,
# Banana = $0.50, Orange = $0.75, Mango = $2.00.
# Store the prices in separate variables.
# Write code that checks if the cart contains a "Mango". If it does, apply a 10% discount to the total price of the cart.
# Calculate the total cost and print the final amount (after applying the discount, if applicable).


# 3)  Inventory System
# You are developing an inventory system for a store.
# When an item is sold, it must be removed from the list,
# and if the list becomes empty, you should notify that the store is out of stock.
#
# Task:
# Create a list called inventory that contains ["Shirt", "Pants", "Socks", "Hat", "Shoes"].
# Remove an item from the list if it gets "sold" (e.g., remove "Hat").
# Write code to check if the list is empty after the removal. If it is empty, print "Out of Stock";
# otherwise, print the remaining inventory.


