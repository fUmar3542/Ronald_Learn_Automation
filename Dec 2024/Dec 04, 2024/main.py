
#####################################################################
# Write a program to compare two strings according to their ASCII
# values and print string 1 is greater than string 2 and vice versa.
#####################################################################


string1 = ""
string2 = ""
ascii_value_one = 0
ascii_value_two = 0

# Solution1
# # Get the 0 index of each string variable.
# # Get the ASCII value of each string variable.
#
# ascii_value_one = ord(string1[0])
# ascii_value_two = ord(string2[0])
#
# # Compare the ASCII values and print out which one is the greatest.
#
# if ascii_value_one > ascii_value_two:
#     print(f"{string1} with ASCII value {ascii_value_one} is greater than {string2} with ASCII value {ascii_value_two}")
# else:
#     print(f"{string2} with ASCII value {ascii_value_two} is greater than {string1} with ASCII value {ascii_value_one}")

#Solution 2
# It should work for all strings with different lengths. First solution for same length,
# and other solution for different string lengths.

# For loop to get the value of each index for each string variable
largest_string = 0

if len(string1) == 0 and len(string2) == 0:
    print("Both string ere empty.")
else:
    if len(string1) > len(string2):
        largest_string = string1
        smallest_string = string2
    else:
        largest_string = string2
        smallest_string = string1

    if string1 != string2:
        check = True
        for i in range(len(smallest_string)):
            ascii_value_one = ord(string1[i])
            ascii_value_two = ord(string2[i])
            if ascii_value_one != ascii_value_two:
                if ascii_value_one > ascii_value_two:
                    print(f"The ascii value of {string1} is greater than {string2} ")
                    check = False
                else:
                    print(f"The ascii value of {string2} is greater than {string1} ")
                    check = False
                break
        if check:
            print(f"The ascii value of {largest_string} is greater {smallest_string}")
    else:
        print(f"The ascii value of {string1} and {string2} are the same.")

# Compare the index from each string, If the index is the same continue the iteration
# If character of the index is not the same, then break

# Get the ASCII values of the two indices and print which one has the greatest value.


#####################################################
# Task
# Reverse the list with the help of indexing/operator

# Task 1
# Do it with the for loop


# Task 2
# Do it in a single line

name = "Umar Farooq"

