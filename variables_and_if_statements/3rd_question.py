"""
Write a program that would:
* allow to enter two numbers.
* Would ask which math operation you want to perform.
* Would print out the result.
"""
import operator as op

print("Welcome to the Python calculator!")
fst_num = int(input("Please enter the first number: "))
scnd_num = int(input("Please enter the second number: "))
opert = input("Which operation would you like to perform (+, -, /, *): ")

if opert == "+":
    print(f"{fst_num} + {scnd_num} =", op.add(fst_num, scnd_num))
elif opert == "*":
    print(f"{fst_num} * {scnd_num} =", op.mul(fst_num, scnd_num))
elif opert == "/":
    print(f"{fst_num} / {scnd_num} =", op.truediv(fst_num, scnd_num))
elif opert == "-":
    print(f"{fst_num} - {scnd_num} =", op.sub(fst_num, scnd_num))
else:
    print("Not a valid operator!")