"""
Create a program that would:
* allow user to enter a year.
* Would check if it's a leap year and print a confirmation if so.
* If the year is not a leap year, print it so.
"""


import calendar

condition = True
while condition:
    year = input("Please enter a year or 'x' to leave: ")

    if year == "x":
        condition = False
        print("Program closed.")
    elif int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
        print("Its a leapyear.")
    else:
        print("Its not a leapyear.")


# Alternative
"""condition = True
while condition:

    year = int(input("Please enter a year: "))
    if year == "x":
        condition = False
        print("Program closed.")
    elif calendar.isleap(year):
        print("It's a leap year!")
    else:
        print("It's not a leap year!")"""


