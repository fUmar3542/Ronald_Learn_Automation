# from that_file_name import calculate

# High Order Function


def calculate(num1, num2):
    print(num1 * num2)


def calculate1(num1, num2, num3):
    print(num1 + num2 * num3)


def high_order_function(nested_function, x, y):
    nested_function(x, y)
    # calculate(x, y)


high_order_function(calculate, 78, 90)


# Operating System Book
