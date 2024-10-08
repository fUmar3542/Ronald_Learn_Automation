

# Exception Handling -> try, except, else, finally

score = input("Enter your score: ")

try:
    score = int(score)
    # many lines
    # many lines
    # many lines
    # many lines
except:
    print("The input given is not a number")

print(score)
