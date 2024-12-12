
# input = 'usd'
# currency_list = ['usd', 'pkr', 'eur', 'jpy']
#
# currency_rates = [0.987, 0.678, 0.567]


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


print(currency_values[5][0])   # USD to EUR
print(currency_values[0][5])    # EUR to USD
