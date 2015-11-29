#kpbocheneke@gmail.com
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def is_alternating(word):
    prev, other = VOWELS, CONSONANTS
    if word[0].upper() in VOWELS:
        prev, other = CONSONANTS, VOWELS
    for w in word:
        if w.upper() not in other:
            return False
        prev, other = other, prev
    return True


def striped_words(text):
    return sum([1 for word in re.split("\W+", text) if len(word) > 1 and is_alternating(word)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
