

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

currency_list = ["eur", "gbp", "jpy", "pkr", "peso", "usd"]
currency_list_join = ','.join(currency_list).upper()
currency_values = [
                    # 0: EUR: 1:GBP, 2:JPY, 3:PKR, 4:PESO, 5:USD
                    [1, 0.954, 0.783, 150.527, 275, 58.01], # EUR
                    [0.954, 1, 0.783, 150.527, 275, 58.01], # GBP
                    [1.5, 4.54, 1, 485, 38.4, 75], # JPY
                    [94.3, 85.4, 473, 1, 74.3, 45.5], # PKR
                    [14.75, 15.27, 275.81, 1, 58.12], # Peso
                    [1.5, 4.54, 485, 38.4, 75, 1], # USD
                ]

check = False
amount_input = 0
user_input_currency = 0
user_input2 = 0
answer = 'yes'
answer_list = ['yes', 'ye', 'ys', 'y','no','n']
start_currency = 0
target_currency = 0

while answer == 'yes':
    while True:
        try:
            user_input_currency = input(f"Enter your currency ({currency_list_join}): ").lower()
            if user_input_currency in currency_list:
                check = True
                start_currency = user_input_currency
                answer = 'no'
                break
            else:
                print(f"Invalid input: accepted entries are only: {currency_list_join}")
        except:
            print("Error: invalid input")

    if check:
        check = False
        while True:
            try:
                user_input2 = input(f"Enter target currency ({currency_list_join}): ").lower()
                if user_input2 in currency_list:
                    check = True
                    target_currency = user_input2
                    break
                else:
                    print(f"Invalid input: accepted entries are only: {currency_list_join}")
            except:
                print("Error: invalid input")

    if check:
        check = False
        while True:
            try:
                amount_input = float(input(f"Enter the amount in {user_input_currency.upper()}: "))
                if amount_input > 0:
                    check = True
                    break
                else:
                    print("Error: input must be greater than 0")
            except:
                print("Error: input must be an integer")
    if check:
        list_index = currency_list.index(user_input_currency)
        index = currency_list.index(target_currency)
        result = amount_input * currency_values[list_index][index]
        display = print(f"{amount_input:.2f} {user_input_currency.upper()} is equal to {result:.2f} {target_currency.upper()}.")

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



