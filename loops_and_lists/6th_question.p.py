"""
Rewrite the 5th exercise so that it would print out all the leap years in a given range.
"""

for year in range(1900, 2101):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)
    else:
        continue
