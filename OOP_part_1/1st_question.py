"""
Write a class which would have parameter "text" and methods that would:
* return the text backwards.
* Return the text in lowercase.
* Return the text in uppercase.
* Return a word by the specified index.
* Return how many words are in text.
* Change a specified word and return the changed text.
* Return how many words, numbers, upper and lower case characters there are in text.
* Additional * rewrite the code so that if while an object is initiated no text is passed, the default text would be
"Zen of Python".
* Additional * rewrite the code so that when an object is printed, it would return a formatted string and not an object.
"""

class Sentence:
    def __init__(self, text="Zen of Python"):
        self.text = text

    def __str__(self):
        return f"This is {self.text}"

    def reverse(self):
        return self.text[::-1]

    def lower(self):
        return self.text.lower()

    def upper(self):
        return self.text.upper()

    def choose_word(self):
        choice = int(input(f"Word to return number: (there are currently {len(self.text.split())} words): "))
        return self.text.split()[choice - 1]

    def word_count(self):
        return f"There are {len(self.text.split())} words in the sentence."

    def change_word(self):
        choice = input(f"Word to change (current text: '{self.text}): ")
        choice2 = input(f"Word to change to: ")
        return self.text.replace(choice, choice2)

    def count_all(self):
        words = len(self.text.split())
        numbers = sum(x.isdigit() for x in self.text)
        upper = sum(x.islower() for x in self.text)
        lower = sum(x.isupper() for x in self.text)
        return (f"In this text there are:\n{words} words\n{numbers} numbers\n{upper} uppercase letters\n{lower}"
                f" lowercase letters")


sentence1 = Sentence()
sentence2 = Sentence("Whoopsie")

print(sentence1.reverse())
print(sentence1.lower())
print(sentence1.upper())
print(sentence1.choose_word())
print(sentence1.word_count())
print(sentence1.change_word())
print(sentence1.count_all())

print(sentence1)
print(sentence2)