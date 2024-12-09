# ########################################################
# # Practice Question 1
# Real-Time Currency Exchange (Finance)
#
# Problem:
# 	Create a currency exchange calculator:
#
# 	Display a menu of available currencies (USD, EUR, GBP, JPY).
# 	Ask the user to input an amount in USD and convert it to the selected currency using these rates:
# 	Validate inputs and repeat until valid.
#
# Sample Run
#
# Input:
# Enter the amount in USD: 100
# Enter the target currency (EUR, GBP, JPY): EUR
#
# Output:
# 100.00 USD is equal to 93.00 EUR.
#
# Would you like to perform another conversion? (yes/no): yes

currency_list = ["eur", "gbp", "jpy", "pkr", "esp"]
currency_list_join = ','.join(currency_list).upper()
currency_values = [0.954, 0.783, 150.527, 275, 58.01]
check = False
user_input = 0
user_input2 = 0
answer = 'yes'
answer_list = ['yes', 'ye', 'ys', 'y','no','n']

while answer == 'yes':
    while True:
        try:
            user_input = float(input("Enter the amount in USD: "))
            if user_input > 0:
                check = True
                break
            else:
                print("Error: input must be greater than 0")
        except:
            print("Error: input must be an integer")

    if check:
         while True:
            try:
                user_input2 = input(f"Enter the target currency ({currency_list_join}): ").lower()
                if user_input2 in currency_list:
                    check = True
                    break
                else:
                    print(f"Invalid input: accepted entries are only: {currency_list_join}")
            except:
                print("Error: invalid input")
    if check:
        index = currency_list.index(user_input2)
        result = user_input * currency_values[index]
        display = print(f"{user_input} USD is equal to {result:.2f} {user_input2.upper()}.")

    while True:
        answer = input("Would you like to perform another conversion? (yes/no): ").lower()
        if answer in answer_list:
            if answer == 'yes' or answer == 'y' or answer == 'ys' or answer == 'ye':
                answer = 'yes'
                break
            else:
                answer = 'no'
                print("End of program")
                break
        else:
            print("Error: Invalid entry. Please enter 'yes' or 'no'.")

# Would you like to perform another conversion? (yes/no): yes


# ########################################################
# # Practice Question 2
# Team Performance Tracker (Sports)
# Problem:
# 	You are tracking the scores of teams in a tournament over multiple games.
#
# 	Represent the data as a nested list where each row is a team's scores in different games.
# 	Compute the average score for each team and find the team with the highest average.
# 	You can use 3 games and 9 teams.
#
# Sample Output
# Input:
# scores = [
#     [89, 76, 91],  # Team 1
#     [78, 85, 88],  # Team 2
#     [92, 81, 79],  # Team 3
#     [84, 77, 90],  # Team 4
#     [88, 92, 94],  # Team 5
#     [70, 65, 75],  # Team 6
#     [95, 91, 89],  # Team 7
#     [82, 87, 85],  # Team 8
#     [80, 79, 78],  # Team 9
# ]
#
# Output:
#
# Team 1 Average Score: 85.33
# Team 2 Average Score: 83.67
# Team 3 Average Score: 84.00
# Team 4 Average Score: 83.67
# Team 5 Average Score: 91.33
# Team 6 Average Score: 70.00
# Team 7 Average Score: 91.67
# Team 8 Average Score: 84.67
# Team 9 Average Score: 79.00
#
# Team 7 has the highest average score of 91.67.
