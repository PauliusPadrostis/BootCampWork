"""
Write a program which would allow:
* a user to enter a number.
* If the number is positive, allow to enter another one.
* If the number is negative, stop the program and print out the sum of all the numbers that were entered.
"""


num_lst = []
while True:
    num = int(input("Please enter a number: "))
    if num > 0:
        num_lst.append(num)
    else:
        print(f"The sum of numbers you entered is: {sum(num_lst)}")
        break

