

# Write a program in which we will be getting 2 inputs from the user gmail, password.
# In case if username and password doesn't exist, the user will be signing up to our platform.

# Get user_email
# validate user email in while loop
# if user email does not exist and is valid, display message: 1) Retry or 2) Signup page
# if user email is valid move to get user password, otherwise, continue to ask for valid input (@ and not blank)
# Get user password
# validate user password in another while loop
# if user password is valid (at least 8 characters), login to website, otherwise, continue to ask for input.

data = {"ronald.johnson@gmail.com": "12345678",
        "suebird@gmail.com": "11122233",
        "michaeljordan@gmail.com": "23232323"}

access_granted = 1

while True:
    if access_granted == 1:
        break
        # exit()
    else:
        user_email = input("Enter email address: ").lower().strip()
        if len(user_email) >= 11 and user_email[-10:] == "@gmail.com" and user_email.count("@") == 1:
            if user_email in data:
                while True:
                    user_password = input("Enter password: ")
                    if data[user_email] == user_password:
                        print("Access granted to website.")
                        access_granted = 1
                        break
                    else:
                        print("Invalid password. Please try again.")
            else:
                print("Email address does not exist in our system.")
                while True:
                    try:
                        user_selection = int(input("Enter: 1) Retry or 2) Signup Page: "))
                        if user_selection == 1:
                            print("Redirecting to home screen.")
                            break
                        else:
                            print("Welcome to the signup page.")
                            # Pending functionality
                            break
                            # exit()
                    except Exception as e:
                        print(f"Error: invalid entry, please enter 1 or 2. {e} ")
        else:
            print("Error: entry must contain @gmail.com, one @ character, and/or length must be greater than 10")


print("Something")