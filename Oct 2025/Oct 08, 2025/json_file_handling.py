import json
import openpyxl
import selenium


# JSON files

# Key value pairs
# list

numbers = [67, 87, 45, 69, 90, 9]

data = {
    '90': {"id": 90, "name": "Ronald", "age": 25},
    '91': {"id": 90, "name": "Ronald", "age": 25},
    '92': {"id": 90, "name": "Ronald", "age": 25}
}

# print(data.get("90"))


# Write
with open("data.json", "w") as file:
    json.dump(data, file)


# Read
with open("data.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data)