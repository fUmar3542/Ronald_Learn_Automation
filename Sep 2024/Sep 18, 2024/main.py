

# ----------------------------------------------

# 3) Create a 2-dimensional list representing seats in a hall
# (e.g., 5 rows and 4 columns). Initialize all seats as "Available"

# Use the append method to add a new row of seats.
# Use the insert/append method to insert a new seat in a specific row (e.g., insert a new seat into the third row at third position).
# Use a conditional statement to check if the first row is fully occupied.
# Print "Row is full" if true, otherwise print "Seats available."

ages = [1, 2, 3, 4]

seats = [
        ["Occupied", "Occupied", "Occupied", "Occupied"],
        ["Available", "Available", "Available", "Available"],
        ["Available", "Available", "Available", "Available"],
        ["Available", "Available", "Available", "Available"],
        ["Available", "Available", "Available", "Available"]
    ]

seats.append(["Available", "Available", "Available", "Available"])
# seats[2].append("Available")
seats[2].insert(2, "Available")

print(len(seats))

if (seats[0][0] == "Available") or (seats[0][1] == "Available") or (seats[0][2] == "Available") or (seats[0][3] == "Available"):
        print("Seats Available.")
else:
        print("Row is full.")


# print(type(seats))
# print(type(seats[0]))
# print(type(seats[0][0]))

# C++
# string name = "Umar";
# string name;
# name = "Umar";

# Python
# name = "Umar"

# Variable declaration vs variable assignment vs variable initialization

# string name;         vs name = "Umar";      vs  string name = "Umar";

# variable initialization = Variable declaration + variable assignment



# # Use the append method to add a new row of seats.
#
#
#
# seats.append(["Row 6"])
#
#
#
# print("")
#
#
#
# print(seats)
#
#
#
# # Use the insert method to insert a new seat in a specific row (e.g., insert a new seat into the third row).
#
#
#
# seats.insert(5,"New Seat")
# print(seats)
#
#
#
# # Use a conditional statement to check if the first row is fully occupied.
# # Print "Row is full" if true, otherwise print "Seats available."
#
#
#
# seats_capacity = len(seats[1])
# print(seats_capacity)
#
#
#
# if seats_capacity >= 4:
# print("Row is full")
# else:
# print("Seats available")
