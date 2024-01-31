"""
Write a program that would allow to:
* enter a number.
* Print if the number is even or odd.
* Print if the number is divisible by 3
"""

str_num = input("Enter your number: ")
num = int(str_num)
if num % 2 == 0:
    print("Number is divisible by 2")
    if num % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible by 3")
else:
    print("Number is not divisible by 2")