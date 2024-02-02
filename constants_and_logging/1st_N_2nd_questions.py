"""
1. Create functions that:

Returns the sum of all given numbers (with *args argument)
Trim the root of the given number (use math.sqrt())
Increase the number of characters in the given sentence (with len())
It would beautify the result by dividing the number x by y
Set the standard logger (logging) so that it:

Save messages to the desired file
Store INFO level messages
Messages must be in the following format: date/time, level, message

2. Redesign the program for Task 1 so that:

Passing a string argument to the root function would save the exception error with the desired text to the log file
Passing 0 as the second argument to the division function would save the exception error with the desired text to the log file
"""

import math
import logging

# QUESTION 1/2
logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


def add(*args):
    logging.info(f"Function: {add.__name__}, returned the sum of passed numbers, which was {sum(args)}")
    return sum(args)


def squared(num):
    try:
        math.sqrt(num)
        logging.info(f"Function: {squared.__name__}, squared number: {num}. Returned: {math.sqrt(num)}")
        return math.sqrt(num)
    except TypeError:
        logging.exception(f"Can't get square root of {num} cause its not a number!\n")


def length(word):
    logging.info(f"Function: {length.__name__}, returned the length of the word {word}, which was {len(word)}")
    return len(word)


def divide(num1, num2):
    try:
        res = num1 / num2
        logging.info(f"Function: {divide.__name__}, divided {num1} by {num2}. Returned: {num1 / num2}")
        return res
    except:
        logging.exception("Not a number!")


print(add(1, 2, 3, 4, 5, 6))
print(squared("A"))
print(length("Make my day!"))
print(divide("a", 2))
