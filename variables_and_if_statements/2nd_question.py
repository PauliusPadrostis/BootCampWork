"""
Write a program that would do the following with the line "Zen of Python":
* print the last symbol of the second word.
* Print the first symbol of the third word.
* Print only the first word.
* Print only the last word.
* Print the whole phrase but backwards.
* Separate the words and print them.
* Change the word "Python" to "Programming" and print the new phrase.
"""


mantra = "Zen of Python"

print(mantra)
print(mantra.split()[1][-1])
print(mantra.split()[2][0])
print(mantra.split()[0])
print(mantra.split()[2])
print(mantra[::-1])
print(mantra.split())
print(mantra.replace("Python", "Programming"))
mantra.casefold()
mantra.lower()