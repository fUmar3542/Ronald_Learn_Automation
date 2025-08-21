
# Tree Recursion

def fib(number):
    if number < 0:
        print("Incorrect number passed...")
        return 0
    if number == 0 or number == 1:
        return number
    return fib(number - 1) + fib(number - 2)


print(fib(10))


# 1-> fib(5)
# 2 -> fib(4)
# 3 -> fib(3)
# 4 -> fib(2)


# Tail Recursion

def print_string_descending(s):
    if not s:
        return
    print(s[-1])
    print_string_descending(s[0:-1])


# Head recursion

def print_string_descending(s):
    if not s:
        return
    print_string_descending(s[0:-1])
    print(s[-1])
