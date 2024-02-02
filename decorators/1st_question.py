"""
Write a decorator that limits the number of parameters (say no more than 2 parameters for a function)
"""


def arg_limiter(function):
    def wrapper(*args):
        if len(args) > 2:
            return "Too many arguments."
        else:
            return function(*args)

    return wrapper


@arg_limiter
def add_nums(*args):
    return sum(args)


@arg_limiter
def multiply_nums(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(add_nums(2, 3))
print(multiply_nums(3, 3))
