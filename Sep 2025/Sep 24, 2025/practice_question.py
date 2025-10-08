

numbers = [9,45,2,3,4,5,6,7,8]


def search(roll_number):
    for item in numbers:
        if roll_number == item:
            return True
    return False


roll_number = 2
print(search(roll_number))