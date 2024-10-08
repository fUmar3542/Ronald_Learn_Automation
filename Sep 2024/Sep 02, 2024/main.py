


# Conditional statements

# if, else, elif

# number = 10
#
# if number < 5:
#     print("")
#     print()
#     print()
# elif number < 10:
#     print()
# else:
#     print()


#
# 8. Temperature Converter
# Create a Python program that converts temperatures between Fahrenheit and Celsius. The program should take two inputs:
# the temperature value and the unit of the temperature ("C" for Celsius or "F" for Fahrenheit).
# The program should print the converted temperature in the other unit.

#
# # Get input
# try:
#     temperature_value = float(input("Enter temperature value: "))
#     unit_of_temperature = input("Enter unit of temperature(Hint: C/F): ")
#     if (unit_of_temperature != 'C') and (unit_of_temperature != 'F'):
#         print("Unit of temperature can only be C or F.")
# except:
#     print("Incorrect input...")
# else:
#     # Calculation
#     # F = 1.8 * C + 32
#     # C = (F - 32) × 5/9
#
#     if unit_of_temperature == 'C':
#         result = 1.8 * temperature_value + 32
#         print("Fahrenheit: " + str(result))
#     else:
#         result = (temperature_value - 32) * 5/9
#         print("Celsius: " + str(result))



# Switch Statement, python -> match case

number = int(input("Enter number which should be a multiple of 10 and less than 50: "))

if number == 10:
    print()
elif number == 20:
    print()
elif number == 30:
    print()
elif number == 40:
    print()
