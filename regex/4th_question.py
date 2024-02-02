"""
Write a function that takes text as parameters and a list of words to censor in it. For example, the word "kvaraba"
is a terrible swear word, and we need to replace it with k*****a in the given text. Start something like this:

def censor(text, *curses):
    # this will be your function

# after calling a function, eg:
censor('horrible words like kvaraba, snakes..', 'kvaraba', 'snakes')
# would be printed for us
# scary words like k*****a, ž****s..
use regex to censor words and use .replace() to replace them in text
"""

import re

text = (
    "Once upon a fucking time, in a small village nestled among rolling hills, there lived a curious young cunt named "
    "Lily. She had an insatiable thirst for cock and loved exploring the world around her. One day, "
    "while wandering through a big ass forest, she stumbled upon an ancient treasure map. Determined to uncover its "
    "secrets, Lily embarked on a daring adventure. With each step, she encountered mysterious assholes, "
    "overcame challenges, and unraveled the hidden clues. Finally, after a bitch of a journey, Lily reached the "
    "spot marked on the map. What she discovered left her fucked, for it was not gold or jewels, but a deep "
    "understanding of her own resilience and courage which she had fuck all")

swear_words = ["fucking", "cock", "ass", "assholes", "bitch", "fucked", "fuck", "cunt"]


def censor_text(text, swear_words):
    for word in swear_words:
        pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.I)
        replacement = word[0] + "*" * (len(word) - 2) + word[-1]
        text = pattern.sub(replacement, text)
    return text


print(censor_text(text, swear_words))
