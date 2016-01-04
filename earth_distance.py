import re
from math import *

R = 6371


def distance(first, second):
    h1, w1 = first.replace(",", "").split(" ")
    h2, w2 = second.replace(",", "").split(" ")

    reg = r"(\d+)°(\d+)′(\d+)″(\D)"

    h1 = re.match(reg, h1).groups()
    h2 = re.match(reg, h2).groups()
    w1 = re.match(reg, w1).groups()
    w2 = re.match(reg, w2).groups()

    h1 = float(h1[0]) + float(h1[0]) / 60 + float(h1[2]) / 3600
    h2 = float(h2[0]) + float(h2[0]) / 60 + float(h2[2]) / 3600
    w1 = float(w1[0]) + float(w1[0]) / 60 + float(w1[2]) / 3600
    w2 = float(w2[0]) + float(w2[0]) / 60 + float(w2[2]) / 3600

    dlat = h2 - h1
    dlon = w2 - w1
    A = pow(sin(dlat / 2), 2) + cos(h1) * cos(h2) * pow(sin(dlon / 2), 2)
    result = R * 2 * atan2(sqrt(A), sqrt(1 - A))
    print(result)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"

    print("All done? Earn rewards by using the 'Check' button!")
