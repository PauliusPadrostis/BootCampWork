"""
Using the provided code:
* rewrite the functions so that they return something.
* Create unit tests for each function (minimum 3 per function).
* Try to improve the functions.
"""
import calendar
import datetime


def num_sum(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


def list_sum(lst):
    num_sum = 0
    for num in lst:
        num_sum += num
    return num_sum


def max_num(*args):
    return max(args)


def reverse_string(string):
    return string[::-1]


def info(string):
    upper = 0
    lower = 0
    nums = 0
    for x in string:
        if x.isupper():
            upper += 1
        if x.islower():
            lower += 1
        if x.isnumeric():
            nums += 1
    return f"Upper: {upper}, lower: {lower}, numbers: {nums}, words: {len(string.split())}"


def unique_only(*args):
    return sorted(list(set(args)))


def is_prime(num):
    if num > 1:
        for x in range(2, num):
            if x % num == 0:
                return False
        return True
    return False


def sort_backwards(sentence):
    words = sentence.split()[::-1]
    return " ".join(words)


def is_leap(year):
    return calendar.isleap(year)



