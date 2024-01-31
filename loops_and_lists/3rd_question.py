"""
Create a program that would:
* allow user to enter 5 words one by one.
* Add entered words to a list.
* Print each word, it's length, and it's place in the list.
*Additional* Allow to user to specify how many words he wants to add.
"""


word_count = int(input("How many words would you like to add: "))
word_list = []

while word_count > 0:
    word = str(input("Please enter a word: "))
    word_list.append(word)
    word_count -= 1

for x in range(len(word_list)):
    print(f"{x + 1}. {word_list[x]} (Length of the word: {len(word_list[x])})")
