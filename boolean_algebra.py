# kpbochenek@gmail.com

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def conv(b):
    print(b)
    if b:
        return 1
    else:
        return 0


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        return conv(x and y)
    elif operation == OPERATION_NAMES[1]:
        return conv(x or y)
    elif operation == OPERATION_NAMES[2]:
        return conv(not x or y)
    elif operation == OPERATION_NAMES[3]:
        return conv(x ^ y)
    else:
        return conv(x == y)


if __name__ == '__main__':
    # These "asserts" using for checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print("All done? Earn rewards by using the 'Check' button!")
