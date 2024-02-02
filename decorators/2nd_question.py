"""
Write a decorator that allows you to pass only string parameters to a function.
"""


def limit_args_to_string(function):
    def wrapper(*args, **kwargs):
        if any(not isinstance(arg, str) for arg in args) or any(
                not isinstance(value, str) for value in kwargs.values()):
            return "Not a string."
        else:
            return function(*args, **kwargs)

    return wrapper


@limit_args_to_string
def count_chars(string):
    return len(string)


print(count_chars(5))
