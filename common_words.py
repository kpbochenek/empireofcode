#kpbochenek@gmail.com
def common_words(first, second):
    dd = set()
    for s in first.split(","): dd.add(s)
    return ",".join(sorted([w for w in second.split(",") if w in dd]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words("one,two,three", "four,five,six") == "", "Too different"
    assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
