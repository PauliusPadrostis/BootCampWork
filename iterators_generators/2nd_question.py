"""
Write a generator that generates one number of the Fibonacci sequence every time. (The sequence starts with the
following numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
Each number in this sequence is equal to the sum of the two preceding numbers, more on google:)
"""


def gen_fib():
    first_num = 0
    second_num = 1
    while True:
        result = first_num + second_num
        yield result
        first_num = second_num
        second_num = result


sequence = gen_fib()

for x in range(100000):
    print(next(sequence), end=",")
