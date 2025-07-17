
num1 = 14
num2 = 18


def print_number(number):
    print(number)


def calculator(number1, number2):

    #############################################################################
    # This function will be returning the sum of the values passed as parameters
    #############################################################################
    def add():
        sum = number1 + number2
        # print_number(sum)
        return sum

    sum = add()
    # print_number(sum)
    # print_number(number1)
    # print_number(number2)

    return sum

sum = calculator(num1, num2)
print_number(sum)



# num1 = 12
# num2 = 16
#
#
# def calculator(val1, val2):
#     print(val1)
#     print(val2)
#
#
# calculator(num1, num2)
