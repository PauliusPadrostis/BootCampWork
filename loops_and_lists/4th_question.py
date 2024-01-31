"""
Create a program that would:
* generate 3 random numbers from 1 to 6.
* If any of the numbers is 5 - print "You lost".
* Otherwise - print "You won".
"""


import random as ran
import itertools

num_list = []
itertools.repeat(num_list.append(ran.randint(1, 6)))

if 5 in num_list:
    print("You lost!")
else:
    print("You won!")


