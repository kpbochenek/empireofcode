# kpbochenek@gmail.com
from math import acos
from math import pi


def angles(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    x = round(acos((a*a + c*c - b*b) / (2 * a * c)) * 180 / pi)
    y = round(acos((b*b + c*c - a*a) / (2 * b * c)) * 180 / pi)
    z = round(acos((a*a + b*b - c*c) / (2 * a * b)) * 180 / pi)
    return sorted([x, y, z])


if __name__ == '__main__':
    # these "asserts" using only for checking and not necessary for testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
