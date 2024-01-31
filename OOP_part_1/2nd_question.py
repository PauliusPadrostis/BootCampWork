"""
Create a class "Anniversaries" which would have a parameter "date" and methods that would:
* print how much time has passed since the date.
* Would return if the year of the date specified was a leap year.
* Would subtract a user specified amount of days from the date and return a new date.
* Would add a user specified amount of days to the date and return a new date.
* Additional * rewrite the code to make it so that if no date is specified, the methods use a default date.
* Additional * rewrite the code so that when an object is printed, it would return a formatted string and not an object.
"""

import datetime
import calendar


class Anniversaries:
    def __init__(self, date: str = "1994-02-23"):
        self.date = date

    def __str__(self):
        return f"This is {self.date}"

    def time_since(self):
        current_time = datetime.datetime.today()
        check_against = datetime.datetime.strptime(self.date, "%Y-%m-%d")
        difference = current_time - check_against
        print(f"{difference.days} days.")
        print(f"{difference.days // 12} months.")
        print(f"{difference.days // 365} years.")

    def is_leap(self):
        if calendar.isleap(int(self.date[0:3])):
            print("Its a leap year")
        else:
            print("It's not a leap year")

    def sub_days(self):
        date = datetime.datetime.strptime(self.date, "%Y-%m-%d")
        to_remove = int(input("How many days to remove: "))
        print(date - datetime.timedelta(days=to_remove))

    def add_days(self):
        date = datetime.datetime.strptime(self.date, "%Y-%m-%d")
        to_remove = int(input("How many days to add: "))
        print(date + datetime.timedelta(days=to_remove))


anniversary1 = Anniversaries("1998-02-23")
Anniversaries.time_since(anniversary1)
Anniversaries.is_leap(anniversary1)
Anniversaries.sub_days(anniversary1)
Anniversaries.add_days(anniversary1)

print(anniversary1)
