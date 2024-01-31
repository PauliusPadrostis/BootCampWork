"""
Write a program that would:
* print the current date and time.
* Subtract 5 days from current date and time and print the result.
* Add 8 hours to current date and time and print the result.
* Print current time and date in format: YYYY MM DD, HH:MM:SS
"""

import datetime

current = datetime.datetime.today()

print(current)
print(current - datetime.timedelta(days=5))
print(current + datetime.timedelta(hours=8))
print(current.strftime("%Y %m %d, %H:%M:%S"))