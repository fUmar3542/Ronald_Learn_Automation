

# Arguments / Parameters


def print_numbers():
    print(1)
    return


def operation():
    num = 10 * 90
    return num
    # return 10 * 90


def operation1():
    num = 10 * 90
    num1 = 10 + 90
    return num, num1


def operation2():
    num = 10 * 90
    num1 = 10 + 90
    names = ["Ronald", "Umar"]
    return num, num1, names


def operation3():
    num = 10 * 90
    if num > 100:
        return 0, 0, []
    num1 = 10 + 90
    names = ["Ronald", "Umar"]
    return num, num1, names


print_numbers()
print_numbers()
print_numbers()

number = operation()
number1 = operation()

number, number1 = operation1()

number, *number1 = operation2()

print(number, number1)
