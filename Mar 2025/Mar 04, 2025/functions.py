

def print_name():
    name = input("Enter name: ")
    print(name)


def print_numbers(number1: int, number2: int) -> None:
    print(number1)
    print(number2)
    return


def return_result(number1: int, number2: int) -> int:
    return number1 + number2, number1 - number2, number1 * number2


print_numbers(number1=10, number2=20)

result1, *result2 = return_result(number1=20, number2=30)

print(result1)

# print_name()


def print_values(**val):
    print(val)


print_values(value1=12, value2=30)
