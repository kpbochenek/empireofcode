# kpbochenek@gmail.com

import math

def simple_areas(*args):
    if len(args) == 1: return round(pow(args[0]/2, 2) * math.pi, 2)
    if len(args) == 2: return round(args[0] * args[1], 2)
    else:
        a, b, c = args[0], args[1], args[2]
        s = (a + b + c) / 2
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    # Rank 1
    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    # Rank 2
    assert almost_equal(simple_areas(5.66, 1.0, 5.66, 9.0), 20.02), "Quadrilateral"
    assert almost_equal(simple_areas(12, 20, 24, 10), 237.72), "Rectangle again"
    assert almost_equal(simple_areas(42, 42, 42, 42), 1764), "Square"

    # Rank 3
    assert almost_equal(simple_areas(5.66, 1.0, 5.66, 9.0, 6.4), 19.98), "Quadrilateral 5"
    assert almost_equal(simple_areas(4.0, 4.0, 7.62, 7.62, 9.9, 5.66), 28.017), "Quadrilateral 6"
