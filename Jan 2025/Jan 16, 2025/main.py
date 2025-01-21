

names = [
        {"first": "umar", "second": "farooq"},
        {"second":"farooq", "first":"umar"}
]

for index, value in enumerate(names):
        print(index)
        print(value["first"])


# names = ["umar", "farooq"]
#
# if "umar" in names:
#         print()
# else:
#         print()

print(names)

names.append({"second":"johnson", "first":"james"})

# p = {"second":"johnson", "first":"james"}
# names.append(p)

# if type(p) == dict:
#         names.append(p)


print(names)

names.append("Umar")

print(names)


name = {"second":78, "first":"james"}

if "second" in name:
        print()

print(name["second"])


tasks = [
        {"status": "completed", "task": "desc", "priority": "low"},
        {"status":"in progress", "task":"desc1", "priority": "low"},
        {"status": "in progress", "task": "desc", "priority": "medium"},
]

# 2 conditions

# status

# 1. 1) completed 2) in progress
# 2. 1) not completed 2) completed
# 3. 1) completed 2) completed
# 4) 1) in progress 2) in progress

a = 2
b = 4

numbers = [1,2,3,4]

# 1)
temp = numbers[1]
numbers[1] = numbers[2]
numbers[2] = temp

# 2)
numbers[1], numbers[2] = numbers[2], numbers[1]





