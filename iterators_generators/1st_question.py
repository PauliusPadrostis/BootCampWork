"""
Write a generator that returns the next even number every time it is initialized with the next function.
The first ch. 2, then 4 and so on without end.
"""


def return_div_2():
    num = 0
    while True:
        yield num
        num += 2

num = return_div_2()

print(next(num))
print(next(num))
print(next(num))
