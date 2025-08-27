

# Decorators

# Decorators are function which we can use to add the functionality before and after the function execution.


name = "Umar"

def my_decorator(func):
    def wrapper():
        print("Before the function call: ")
        func()
        print("After the function call: ")
    return wrapper()


@my_decorator
def say_my_name():
    print("Ronald!")
    print(name)


@my_decorator
def say_hello():
    global name
    name = "Farooq"
    print("HELLO!")
    print(name)


# # print("Before the function call: ")
# say_hello()
# # print("After the function call: ")
#
# # print("Before the function call: ")
# say_my_name()
# # print("After the function call: ")



# Shallow Copy and Deep Copy

number1 = [1,23,4,4,5,67]

number2 = number1[0:]

print(number1)
print(number2)

number2[2] = 56

print(number2)
print(number1)


import copy

number3 = copy.copy(number1)

number3[2] = 100

print(number1)
print(number3)

number4 = copy.deepcopy(number1)
