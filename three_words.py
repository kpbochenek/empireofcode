# kpbochenek@gmail.com

def three_words(words):
    result = 0
    for w in words.split(" "):
        if w[0].isnumeric():
            result = 0
        else:
            result += 1
            if result >= 3:
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"
