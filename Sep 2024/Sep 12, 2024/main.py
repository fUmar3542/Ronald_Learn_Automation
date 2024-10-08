

# ******************************************************************

credit_card_input = input("Enter your credit card number: ")
credit_card_length = len(credit_card_input)

try:
    if credit_card_length != 16:
        print("Invalid credit card number")
    elif credit_card_input.isnumeric() is False:
        print("Invalid credit card number")
    elif credit_card_input[0] != '4' and credit_card_input[0] != '5' and credit_card_input[0] != '6':
        print("Invalid credit card number")
    elif credit_card_input.isspace() is True:
        print("Invalid credit card number")
    else:
        print("Valid credit card number")
except:
    print("Error")


# ******************************************************************

# const
# C++ -> const string currency = 'USD';
# C++ -> arrays, linklist
# arrays -> collection of similar elements or of same data types
# linklist -> chain of elements but connected with pointers


# Collection of elements

name1 = "name1"
name2 = "name1"
name3 = "name1"
name4 = "name1"
name5 = "name1"

# name = ["name1", "name2", "name3", "name4", "name5"]

name = []

# list vs tuple vs set

# list -> mutable, ordered data structure, allow duplicates
# tuple -> immutable, ordered,  allow duplicates
# Set -> mutable, unordered,  no duplicates allowed
