"""
Write a program that would:
* allow to enter numbers a and b.
* Would check if a is less than b and print if so.
* Would check if a is equal to b and print if so.
* Would check if a is more than b and print if so.
"""

a = float(input("Enter the first number : "))
b = float(input("Enter the second number: "))

if a > b:
    print("The first number is higher than the second one.")
elif a < b:
    print("The second number is higher than the first one.")
else:
    print("Both numbers are equal")