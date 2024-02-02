"""
Using the provided code:
* rewrite the methods so that they return something.
* Create unit tests for each method (minimum 3 per function).
* Try to improve the methods.
"""


class Sentence:
    def __init__(self, text="Zen of Python"):
        self.text = text

    def __str__(self):
        return "Text: " + self.text

    def backwards(self):
        return self.text[::-1]

    def upper(self):
        return self.text.upper()

    def lower(self):
        return self.text.lower()

    def search(self, word):
        return self.text.count(word)

    def change(self, old, new):
        return self.text.replace(old, new)

    def print_word(self, num):
        text_sorted = self.text.split()
        return text_sorted[num]

    def info(self):
        words = len(self.text.split())
        numbers = sum(i.isnumeric() for i in self.text)
        upper = sum(i.isupper() for i in self.text)
        lower = sum(i.islower() for i in self.text)
        return f"Words: {words}, numbers: {numbers}, upper: {upper}, lower: {lower}"
