# 1. First task - Celsius to Fahrenheit and Kelvin

celsius_temperature = float(input('Please enter a Celsius temperature to convert to Fahrenheit and Kelvin: '))
fahrenheit_temperature = round(((celsius_temperature * 9/5) + 32), 2)
kelvin_temperature = round((celsius_temperature + 273.16), 2)
print("Fahrenheit temperature: " + str(fahrenheit_temperature) + " °F",
      "Kelvin temperature: " + str(kelvin_temperature) + " K",
      sep='\n')
# print(f'Fahrenheit temperature: {fahrenheit_temperature} °F', # Just tried another way to print
#       f'Kelvin temperature: {kelvin_temperature} K',
#       sep='\n')

# 2. Second task - Volume and Temperature

# first_mix_volume = float(input('Please enter volume of the first mix: '))
# first_mix_temperature = float(input('Please enter temperature of the first mix: '))
# second_mix_volume = float(input('Please enter volume of the second mix: '))
# second_mix_temperature = float(input('Please enter temperature of the second mix: '))
# together_mix_volume = round((first_mix_volume + second_mix_volume), 2)
# together_mix_temperature = round(((first_mix_volume * first_mix_temperature
#                                    + second_mix_volume * second_mix_temperature)
#                                   / together_mix_volume), 2)
# print("General volume: " + str(together_mix_volume),
#       "General temperature: " + str(together_mix_temperature),
#       sep='\n')
# # print(f'General volume: {together_mix_volume}', # Just tried another way to print
# #       f'General temperature: {together_mix_temperature}',
# #       sep='\n')

# 3. Third task - Currency conversion

# uah_to_usd_rate = 0.027
# uah_to_eur_rate = 0.025
#
# currency_convert_from = input("Select the currency to convert from (UAH, USD, EUR): ").upper()
# currency_convert_to = input("Select currency to convert to (UAH, USD, EUR): ").upper()
# amount = input("Please enter an amount to convert: ")
#
# try:
#     amount = float(amount)
#     if currency_convert_from == "" or currency_convert_to == "":
#         print('Currency fields cannot be empty. Please fill in all the required fields to do the conversion.')
#     elif currency_convert_from not in ["UAH", "USD", "EUR"] or currency_convert_to not in ["UAH", "USD", "EUR"]:
#         print('This operation is not supported, please try again')
#     elif (currency_convert_from == "UAH" and currency_convert_to == "UAH") \
#             or (currency_convert_from == "USD" and currency_convert_to == "USD") \
#             or (currency_convert_from == "EUR" and currency_convert_to == "EUR"):
#         print("This conversion is not supported. Please enter different currencies.")
#     elif amount < 0:
#         print('Amount cannot be negative. Please enter a positive number.')
#     else:
#         if currency_convert_from == "UAH" and currency_convert_to == "USD":
#             converted_amount = round((amount * uah_to_usd_rate), 2)
#             print("UAH: " + str(amount) + "₴", "=> USD: " + str(converted_amount) + "$")
#         elif currency_convert_from == "UAH" and currency_convert_to == "EUR":
#             converted_amount = round((amount * uah_to_eur_rate), 2)
#             print("UAH: " + str(amount) + "₴", "=> EUR: " + str(converted_amount) + "€")
#         elif currency_convert_from == "USD" and currency_convert_to == "UAH":
#             converted_amount = round((amount / uah_to_usd_rate), 2)
#             print("USD: " + str(amount) + "$" + "₴", "=> UAH: " + str(converted_amount) + "$")
#         elif currency_convert_from == "EUR" and currency_convert_to == "UAH":
#             converted_amount = round((amount / uah_to_eur_rate), 2)
#             print("EUR: " + str(amount) + "€", "=> UAH: " + str(converted_amount) + "₴")
#         else:  # I'm not sure if this else is needed
#             print('Something went wrong, please try again')
# except ValueError:
#     print('Amount cannot be empty. Please enter a positive number.')

# 4. Fourth task - Simple calculator

# first_number = input("Enter your first number: ")
# operation_to_do = input("Enter operation you would like to do (+, -, *, /): ")
# second_number = input("Enter your second number: ")
#
# if not all([first_number, second_number, operation_to_do]):
#     print('Input and operation cannot be empty')
# else:
#     try:
#         first_number = float(first_number)
#         second_number = float(second_number)
#         if operation_to_do == '+':
#             print(first_number + second_number)
#         elif operation_to_do == '-':
#             print(first_number - second_number)
#         elif operation_to_do == '*':
#             print(first_number * second_number)
#         elif operation_to_do == '/':
#             if second_number == 0:
#                 print('Cannot divide by zero')
#             else:
#                 print(first_number / second_number)
#         else:
#             print("Invalid operator")
#     except ValueError:
#         print('Invalid input. Please enter a number.')
