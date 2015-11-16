# kpbochenek@gmail.com

def count_inner(v, elements):
    return len(list(filter(lambda x: x < v, elements)))

def count_inversion(seq):
    return sum([count_inner(seq[i], seq[i:]) for i in range(len(seq))])
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
