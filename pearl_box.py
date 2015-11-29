# kpbochenek@gmail.com


cache = {}


def count(marbles, step):
    ctest = (marbles.count('w'), marbles.count('b'), step)
    if ctest in cache: return cache[ctest]
    if step == 0: return (marbles.count('w') / len(marbles), 1)
    wp, c = 0, 0
    for i in range(len(marbles)):
        if marbles[i] == 'b':
            (wpx, cx) = count(marbles[:i] + 'w' + marbles[i+1:], step-1)
        else:
            (wpx, cx) = count(marbles[:i] + 'b' + marbles[i+1:], step-1)
        wp, c = wp+wpx, c+cx
    cache[ctest] = (wp, c)
    return (wp,c)

def probability(marbles, step):
    (wp, c) =  count(marbles, step-1)
    return round(wp / c, 2)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"
