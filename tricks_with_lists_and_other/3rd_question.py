"""
Given list: sarasas = [2.5, 2, "Hello", True, 5, 7, 8, 2.8, "Evening"]

Create an app that:

The sum of all the numbers in the list would be calculated and printed
It would add and print all the words in the list
Counts and prints the number of boolean variables in the list with the value True
Advices:

Use filter or comprehension, sum, " ".join()
"""


lst = [2.5, 2, "Hello", True, 5, 7, 8, 2.8, False, False, "Yard", 60, 1.5, 15.0, "Evening"]

# 3.1
filtered_nums = list(filter(lambda x: type(x) in (int, float), lst))
print(sum(filtered_nums))

# 3.2
filtered_words = list(filter(lambda x: type(x) is str, lst))
print(filtered_words)

# 3.3
print(len(list(filter(lambda x: type(x) is bool, lst))))
print(sum(list(filter(lambda x: type(x) is bool, lst))))



