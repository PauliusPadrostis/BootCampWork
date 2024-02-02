"""
Imagine having to crack a 4-digit pin code. Write a generator that will check the combination one at a time,
starting with 0000, and stop when the pin is correct. Start the program with (eg) PIN = '0549' and continue typing.
After the function is finished, iterate over the created generator with a for loop to print the numbers in sequence
and after printing the last one, write 'PIN is XXXX(their pin)'. Note that the code may start with zero.
Figure out how to work around this problem :).
"""


pin = '1994'


def num_generator():
    for x in range(0, 10):
        for xx in range(0, 10):
            for xxx in range(0, 10):
                for xxxx in range(0, 10):
                    yield f"{x}{xx}{xxx}{xxxx}"


nums = num_generator()
pin_combs = []

for x in range(10000):
    pin_combs.append(next(nums))

for x in pin_combs:
    if x == pin:
        print(f"Your pin is {x}")
        break
    else:
        continue








