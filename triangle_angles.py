def angles(a, b, c):
    return [0, 0, 0]


if __name__ == '__main__':
    # These "asserts" using only for checking and not necessary for testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
