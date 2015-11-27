VOWELS = "aeiouy"

def translate(phrase):
    result = []
    skip = 0
    for w in phrase:
        if skip > 0:
            skip -= 1
            continue
        if w in VOWELS:
            result += w
            skip = 2
        elif w == ' ':
            result += ' '
            skip = 0
        else:
            result += w
            skip = 1
    return "".join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(translate("hoooowe yyyooouuu duoooiiine"))
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
