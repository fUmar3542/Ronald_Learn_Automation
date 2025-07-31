

# Anonymous Function / Lambda Function

# lambda paramaters separated by commas: perform and return the calculated result
multiply = lambda num1: num1 * 8

print(multiply(9))


calculate = lambda num1, num2: num1 * (num2 -10) / 2


# Sorted Function

numbers = [1,4,3,23,54,13,25]
print(sorted(numbers, reverse=True))

student_data = [
    {"name": "Stanley", "marks": 78, "grade": "C"},
    {"name": "Ronald", "marks": 88, "grade": "C"},
    {"name": "Umar", "marks": 79, "grade": "C"},
]

student_data = sorted(student_data, key=lambda student: student['marks'])

for item in student_data:
    print("------------------------------------")
    print(f"Name: {item['name']}")
    print(f"Marks: {item['marks']}")
    print(f"Grade: {item['grade']}")
    print("------------------------------------")


# Filter

emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@jwsjfwek.com", "f", "sbfjwebjkf", "io.com"]

print(list(filter(lambda email: "@" in email and ".com" in email, emails)))


# While returning function

def calculate(n):
    return lambda x: x * n

function = calculate(7)

print(function(8))
