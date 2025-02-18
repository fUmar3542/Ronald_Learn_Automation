from typing import Tuple, Union


# With multiple values return

name_list = ["Ronald", "Michael", "James", "Sally"]


def validity_check1(name1 : str, student_id1 : int) -> Tuple[bool, str]:
    if name1 in name_list and 0 < student_id1 < 100:
        return True, name1
    return False, name1


result, result1 = validity_check1("umar", "12")

print(type(result))
print(result)


# Unpack the collections

numbers_tuple = (1, 2, 3, 4, 5)

# print(numbers_tuple[0])

# var1 = numbers_tuple[0]
# var2 = numbers_tuple[1]
# var3 = numbers_tuple[2]
# var4 = numbers_tuple[3]
# var5 = numbers_tuple[4]

var1, var2, var3, var4, var5 = numbers_tuple

# print(var1)
# print(var2)
# print(var3)
# print(var4)
# print(var5)

var1, var2, var3, *var4 = numbers_tuple

print(var1)
print(var2)
print(var3)
print(var4)
# print(var5)


# Return one value of diff data type


def validity_check1(name1 : str, student_id1 : int) -> Union[bool, str]:
    if name1 in name_list and 0 < student_id1 < 100:
        return name1
    return False


result = validity_check1("Ronald", 12)
print(type(result))
print(result)


#################################################################################################

# Arbitrary arguments/parameters
# *, **
# *args, **kwargs


# def add(num1: int, num2: int, num3: int) -> int:
#     return num1 + num2 + num3
#
#
# def add(num1: int, num2: int) -> int:
#     return num1 + num2
#
#
# print(add(1, 3, 6))
# print(add(1, 3))


def add2(num1: int, num2: int) -> int:
    return num1 + num2


def add3(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


def add4(num1: int, num2: int, num3: int, num4: int) -> int:
    return num1 + num2 + num3 + num4


print(add2(1, 3))
print(add3(1, 3, 6))
print(add4(1, 3, 6, 5))


#  C++, C#, C  -> templates
# The dynamic function which can work with multiple positional parameters.

# <template T>
# int add(T num1){};

# <template T>
# int add(T num1, T num2){};


def add(*numbers):
    # print(type(numbers))
    # print(numbers)

    # result = 0
    # for x in numbers:
    #     result += x
    # return result

    return sum(numbers)


print(add(1))
print(add(1, 2))


def find_avg_and_display(*numbers, student_name):
    print(f"Student Name: {student_name}")
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")


find_avg_and_display(96, 89, 78, 99, 88, "Ronald")
