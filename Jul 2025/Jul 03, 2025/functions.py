

# scope of variables

# 1) Global

COUNT = 15

def return_sum(num1, num2):
    sum = num1 + num2
    if sum == 10:
        return sum
    global COUNT
    COUNT = sum * 4
    return COUNT

print(COUNT)

print(return_sum(3,4))

print(COUNT)


# 2) Local

def return_sum1(num1, num2):
    sum1 = num1 + num2
    return sum1


print(return_sum1(1, 89))

print(sum1)


# nested functions
# lambda
# recursion
# high order functions
# @decorator
# pass by value vs pass by reference
# shallow copy vs deep copy