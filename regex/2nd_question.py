"""
Print a list of dates from this text. Use regular expressions. The dates should be in the format: Month day, year.
"""

import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''


def return_dates(text):
    pattern = re.compile(r"\b[A-Za-z]+\s+\d{1,2},\s+\d{4}\b")
    result = pattern.findall(text)
    for x in result: print(x)


return_dates(text)
