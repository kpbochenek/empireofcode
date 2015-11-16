# kpbochenek@gmail.com

values = [str(i) for i in range(10)] + [chr(l) for l in range(ord('A'), ord('Z') + 1)]


def convert(str_number, radix):
    vals = values[:radix]
    for i in str_number:
        if i not in vals:
            return -1
    return sum([vals.index(e) * pow(radix, idx) for idx, e in enumerate(reversed(str_number))])


if __name__ == '__main__':
    # These "asserts" using only for self-checking necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"
    print("Use 'Check' to earn sweet rewards!")
