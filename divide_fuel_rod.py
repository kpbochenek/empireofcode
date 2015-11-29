# kpbochenek@gmail.com


def trns():
    """ calculates triangular numbers up to 1000"""
    result = []
    c = 0
    for i in range(1000):
        c = c+i
        if c > 2000: break
        result.append(c)
    return result[1:]
trnsx = trns()


def disjoint(number):
    best = []
    for start in range(len(trnsx)):
        current = 0
        result = []
        i = start
        while current < number:
            current += trnsx[i]
            result.append(trnsx[i])
            i += 1

        if current == number and len(result) > len(best):
            best = result
    return best


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disjoint(64) == [15, 21, 28], "1st example"
    assert disjoint(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert disjoint(225) == [105, 120], "1st example"
    assert disjoint(882) == [], "1st example"
    assert disjoint(994) == [], "??"
    assert disjoint(10) == [1, 3, 6], "??"
