"""
We have the following code:

import requests # we import requests
from time import time # we import the time module

start_time = time() # we fix the start time
r = requests.get('http://www.cnn.com') # we make an http request
print(r.status_code) # we print the status code (200 = OK, 404 = Not Found, etc. you can search for http status codes)
end_time = time() # capture the end time
print(end_time - start_time) # print the time it took to get the response
Write a decorator to capture the execution time of any function. You can improve, for example, functions (name),
with such and such arguments execution time - XX s. Test it with a function that returns the site's response code
and with a function that selects prime numbers in a given range.
"""

import requests
from time import time


def func_exec_time(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        function_result = function(*args, **kwargs)
        stop_time = time()
        print(f"Function '{function.__name__}' executed in {stop_time - start_time}")
        return function_result

    return wrapper


@func_exec_time
def return_status_code(website):
    response = requests.get(website)
    return response.status_code


print(return_status_code("https://delfi.lt"))


# @func_exec_time
# def return_primes(from_num, to_num):
#     primes = []
#     for num in range(from_num, to_num):
#         if num > 1 and all(num % x != 0 for x in range(2, int(num**0.5) + 1)):
#             primes.append(num)
#     return primes

@func_exec_time
def return_primes(from_num, to_num):
    is_prime = [True] * (to_num + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(to_num ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * 2, to_num + 1, num):
                is_prime[multiple] = False

    primes = [num for num in range(from_num, to_num) if is_prime[num]]
    return primes


print(return_primes(0, 10000))
