"""
Create a program that returns
the current exchange rate for an input currency pair. Use https://api.frankfurter.app/.
Documentation can be found here. The result might look like this:

get_rate('EUR', 'GBP')
# EUR-GBP: 0.84828

get_rate('ZZZ', 'GBP')
# Incorrectly aggregated currencies. List of possible options:
# ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR',
"""

import requests
import json


def get_rate(curr1, curr2):
    r = requests.get(f'https://api.frankfurter.app/latest?from={curr1}&to={curr2}')
    rr = requests.get(f'https://api.frankfurter.app/latest?from=EUR')

    currency_list = ['EUR', ]

    value2 = json.loads(rr.text)
    for item in value2['rates']:
        currency_list.append(item)

    value = json.loads(r.text)

    if curr1 not in currency_list or curr2 not in currency_list:
        print(f'Wrong currency entered.\nAvailable currencies:')
        for curr in currency_list:
            print(curr)
    else:
        print(f'{curr1}-{curr2}: {value['rates'][f"{curr2}"]}')


get_rate("EUR", "ZAR")