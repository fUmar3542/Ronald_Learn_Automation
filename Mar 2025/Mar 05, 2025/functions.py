

def print_values(**val):
    # print(type(val))
    # print(val)
    for key in val:
        print(key, val[key])

    print(val.keys())
    print(val.values())

    print(val.items())

    for key, value in val.items():
        print(key, value)


print_values(value1=12, value2=30)


############################################################################################

# Recursive functions

# The type of function which can call itself

def print_numbers(num):
    if num == 100:
        return
    print(num)
    print_numbers(num + 1)

# 50 -> print(50)
# 51 -> print(51)
# 52 -> print(52)
# ...
# 100


def print_numbers(num):
    print(num)
    if num == 100:
        return
    print_numbers(num + 1)

# 50 -> print(50)
# 51 -> print(51)
# ...
# 100 -> print(100)
# stop the recursive call


def print_numbers(num):
    if num == 100:
        return
    print_numbers(num + 1)
    print(num)
    return

# 50 -> 51 -> 52 -> 53 -> 54 -> ... -> 98 -> 99

# 99
# 98
# 97
# ...
# 50

print()
print_numbers(50)
print()
