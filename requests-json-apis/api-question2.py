"""
Using the same Frankfurter API (as in the first task), create a program that finds the days when the rate was the
highest and when the rate was the lowest, based on the currency pairs given in the parameters,
the start date and the end date of the period.

currency_pair_analysis('EUR', 'GBP', '2019-01-01', '2019-12-31')

    # In the currency pair EUR-GBP, in the period from 01/01/2019 to 12/31/2019:
    # The lowest rate was 09/12/2019 - 0.84116
    # The highest rate was 08/12/2019 - 0.92203
"""

import requests
import json


def get_high_low_rates(curr1, curr2, s_date, e_date):
    r = requests.get(f'https://api.frankfurter.app/{s_date}..{e_date}?from={curr1}&to={curr2}')
    value = json.loads(r.text)

    print(f'\nIn the currency pair {curr1}-{curr2}, in the period from {value["start_date"]} to {value["end_date"]}:\n')

    curr_highest = -float('inf')
    curr_lowest = float('inf')
    highest_pair = ''
    lowest_pair = ''

    for date, rates in value['rates'].items():
        value_rate = rates[curr2]
        if value_rate > curr_highest:
            curr_highest = value_rate
            highest_pair = f'{date} - {value_rate}'
        if value_rate < curr_lowest:
            curr_lowest = value_rate
            lowest_pair = f'{date} - {value_rate}'

    print(f'The highest rate was {highest_pair}')
    print(f'The lowest rate was {lowest_pair}')



get_high_low_rates('EUR', 'USD', '2023-01-01', '2024-01-30')

