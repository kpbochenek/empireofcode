# kpbochenek@gmail.com


MAX_VAL = 20*20+5


def increase(counter, sides, max_val):
    tmp = [0 for i in range(MAX_VAL)]
    for i in range(1, sides+1):
        for c in range(len(counter)):
            if counter[c] != 0:
                tmp[c + i] += counter[c]
    return tmp


def probability(dice_number, sides, target):
    max_val = 1
    counter = [0 for i in range(MAX_VAL)]
    for i in range(1, sides+1):
        counter[i] = 1
    for d in range(dice_number-1):
        counter = increase(counter, sides, max_val)

    if target < len(counter):
        return round(counter[target] / sum(counter), 4)
    else:
        return 0


if __name__ == '__main__':
    # These are only for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum two 6-sided"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
