
# Homework
# Write a python program to get int or float from the user
# until the user enters 0. When the user will be writing 0,
# you'll be printing the largest, the smallest and the sum of
# all the numbers.


sentinal_value = 0
user_input = 1
input_sum = user_input
largest_number = user_input
smallest_number = user_input
iteration_number = 0

while user_input != sentinal_value:          # Sentinal value
    try:
        user_input = float(input("Enter a number: "))
        if iteration_number == 0:
            smallest_number = user_input
            largest_number = user_input
            iteration_number = 1
        if user_input != sentinal_value:
            input_sum = input_sum + user_input
            if user_input > largest_number:
                largest_number = user_input
            if user_input < smallest_number:
                smallest_number = user_input
    except:
        print("Error: please enter a valid number")


# largest_number = input_list[0]
# smallest_number = input_list[0]
#
# for number in input_list[:-1]:
#     if number > largest_number:
#         largest_number = number
#     if number < smallest_number:
#         smallest_number = number

print("")
print(f"Sum: {input_sum}")
print(f"Largest Number: {largest_number}")
print(f"Smallest Number: {smallest_number}")

