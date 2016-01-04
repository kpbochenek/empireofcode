# kpbochenek@gmail.com


def check_pangram(text):
    v = [False for i in range(ord('a'), ord('z')+1)]
    for l in text.lower():
        if l >= 'a' and l <= 'z':
            v[ord(l) - ord('a')] = True
    return all(v)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

    print("All done? Earn rewards by using the 'Check' button!")
