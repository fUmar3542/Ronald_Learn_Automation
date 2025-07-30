

numbers = [92, 54, 34, 27, 87, 56]


# Bubble sort

for i in range(0, len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


print(numbers)