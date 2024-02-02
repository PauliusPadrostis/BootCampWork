"""
Create an app that:

The Zen of Python would add an exclamation point to each word in the sentence and print a new sentence.
Advices:

Use map (with lambda) or comprehension, " ".join()
"""


sentence = "The Zen of Python"

connected = " ".join(list(map(lambda x: "!" + x, sentence.split(" "))))
print(connected)