"""
Write a program that would:
* allow the user to enter a number.
* Print "True" if number is positive.
* Print "False" if number is negative or equal to 0.
*Additional* rewrite the program to catch exceptions using try/except.
"""

while True:

    try:
        num = int(input("Please enter a number: "))
        if type(num) in [int, float] and num >= 0:
            print(True)
        else:
            print(False)
    except ValueError:
        print("That is not a number! Try again.")
