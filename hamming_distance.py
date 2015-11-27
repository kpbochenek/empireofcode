def hamming(n, m):
    n = bin(n)[2:]
    m = bin(m)[2:]
    m = m.rjust(max(len(m), len(n)), '0')
    n = n.rjust(max(len(m), len(n)), '0')
    return sum([1 for (x,y) in zip(m, n) if x != y])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"
