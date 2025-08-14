

# # Print numbers from 1 to n
def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n)


print_number(20)


# Print the characters in a string in an ascending and descending order.

n = 1
# Descending
def print_string_descending(s):
    if not s:
        return
    print(s[-1])
    print_string_descending(s[0:-1])


# Ascending
def print_string_ascending(s):
    if not s:
        return
    print_string_ascending(s[0:-1])
    print(s[-1])


s = "Ronald"
# print(s[2])
# print(s[0:-1])
# print(s[1:])


print_string_descending("Ronald")
print_string_ascending("Ronald")


# Practice 01:
# You need to write a recursive function to find the fictorial of the accepted paramter.


# Practice 02:
# You need to write a recursive function to find the fibonacci value.