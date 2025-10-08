import csv


# csv files

# list

numbers = [
    [67, 87, 45, 69, 90, 9],
    [67, 87, 45, 69, 90, 9],
    [67, 87, 45, 69, 90, 9],
    [67, 87, 45, 69, 90, 9],
]

# Write
# with open("csv_data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(numbers)

# with open("csv_data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)

with open("csv_data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)


# Read
with open("csv_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)