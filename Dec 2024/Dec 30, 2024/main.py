

user_input = input("Enter numbers: ").split()

# # 1st
# resultant_list = []
# for x in user_input:
#     resultant_list.append(int(x))
#
# # 2nd
# for i in range(len(user_input)):
#     user_input[i] = int(user_input[i])

# numbers = [1,2,3,4]
# for item in numbers:
#     string_list.append(str(item))
# string_list = [str(item) for item in numbers]

# 3rd
# user_input = [int(x) for x in user_input]

# 4th

# map -> iterable to go through the elements one by one
user_input = list(map(int, input("Enter numbers: ").split()))

print(user_input)

print(type(user_input))
