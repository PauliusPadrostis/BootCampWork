"""
Create an app that:

Creates a list of numbers from 0 to 50
Would multiply all the numbers in the list by 10 and print
Pick numbers from the list that are divisible by 7 and print
It would square all the numbers in the list and print it. Assign this list (list array) to a new variable.
With a list of squares (a new variable) would do the following: print the sum, minimum and maximum number, mean, median
List of squares sorted and printed backwards
Advices:

Use map, filter or comprehension, sum, min, max, mean, median, %
from statistics import mean, median
"""



# 2.1
from statistics import mean, median

nums = [x for x in range(1, 51)] # list(range(0, 51))
# 2.2
nums_times_ten = list(map(lambda x: x * 10, nums))
print(nums_times_ten)
# 2.3
divisible_by_7 = list(filter(lambda x: x % 7 == 0, nums_times_ten))
print(divisible_by_7)
# 2.4
divisible_by_7_squared = list(map(lambda x: x ** 2, divisible_by_7))
print(divisible_by_7_squared)
# 2.5
print(sum(divisible_by_7_squared))
print(min(divisible_by_7_squared))
print(max(divisible_by_7_squared))
print(mean(divisible_by_7_squared))
print(median(divisible_by_7_squared))

