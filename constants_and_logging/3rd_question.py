"""
Rewrite the program for Task 2 so that:

A logger of its own would be created to record all the messages described above
The created logger would not only save the messages to a file, but also display them on the console
"""


import math
import logging


class DebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


class CriticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.CRITICAL


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
# Debug:
file_handler_debug = logging.FileHandler("debug.log")
file_handler_debug.setLevel(logging.DEBUG)
# Info:
file_handler_info = logging.FileHandler("info.log")
file_handler_info.setLevel(logging.INFO)
# Warning:
file_handler_warning = logging.FileHandler("warning.log")
file_handler_warning.setLevel(logging.WARNING)
# Error:
file_handler_error = logging.FileHandler("error.log")
file_handler_error.setLevel(logging.ERROR)
# Critical:
file_handler_critical = logging.FileHandler("critical.log")
file_handler_critical.setLevel(logging.CRITICAL)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler_debug.setFormatter(formatter)
file_handler_info.setFormatter(formatter)
file_handler_warning.setFormatter(formatter)
file_handler_error.setFormatter(formatter)
file_handler_critical.setFormatter(formatter)

# Apply the custom filter to the file handler
file_handler_debug.addFilter(DebugFilter())
file_handler_info.addFilter(InfoFilter())
file_handler_warning.addFilter(WarningFilter())
file_handler_error.addFilter(ErrorFilter())
file_handler_critical.addFilter(CriticalFilter())

# Add the file handler to the logger
logger.addHandler(file_handler_debug)
logger.addHandler(file_handler_info)
logger.addHandler(file_handler_warning)
logger.addHandler(file_handler_error)
logger.addHandler(file_handler_critical)


def add(*args):
    logger.info(f"Function: {add.__name__} - |returned the sum of passed numbers, which was {sum(args)}|")
    return sum(args)


def squared(num):
    logger.debug(f"Function: {squared.__name__} - |squared number: {num}. Returned: {math.sqrt(num)}|")
    return math.sqrt(num)


def length(word):
    logger.warning(f"Function: {length.__name__} - |returned the length of the word {word}, which was {len(word)}|")
    return len(word)


def divide(num1, num2):
    logger.error(f"Function: {divide.__name__} - |divided {num1} by {num2}. Returned: {num1 / num2}|")
    return num1 / num2


print(add(1, 2, 3, 4, 5, 6))
print(squared(100))
print(length("Make my day!"))
print(divide(7, 2))
