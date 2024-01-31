"""
Write a program that would:
* allow user to enter a date and time.
* Print out how much time has passed since the entered date. (how many years, months, days, and so on.)
*Additional* rewrite the program to catch exceptions using try/except.
"""

from datetime import datetime, time

while True:

    try:
        user_date = input("Please enter a date (YYYY-MM-DD): ")
        user_date_formatted = datetime.strptime(user_date, "%Y-%m-%d")
        if user_date_formatted > datetime.today():
            print("Date cannot be higher than today's date")
            continue
    except ValueError:
        print("Date was entered incorrectly. Try again.")
        continue
    break

while True:
    try:
        user_time = input("Please enter a time (HH:MM:SS): ")
        hours, minutes, seconds = map(int, user_time.split(":"))
        if 23 >= hours >= 0 >= minutes >= 59 and 0 >= seconds >= 59:
            print("There seems to be too many hours/minutes/seconds. Please enter in the correct format.")
            continue
        user_time_formatted = time(hours, minutes, seconds)
    except ValueError:
        print("Invalid time format. Please enter a time in HH:MM:SS format.")
        continue

    date_time = datetime.combine(user_date_formatted, user_time_formatted)

    current_time = datetime.today()

    print(f"Time elapsed from date entered:\n"
          f"\nYears:{abs(current_time.year - date_time.year)}"
          f"\nMonths: {abs(current_time.month - date_time.month)}"
          f"\nDays: {abs(current_time.day - date_time.day)}"
          f"\nHours: {abs(current_time.hour - date_time.hour)}"
          f"\nMinutes: {abs(current_time.minute - date_time.minute)}"
          f"\nSeconds: {abs(current_time.second - date_time.second)}")
    break