def b(c,p):return (p[1],c+max(p))
def golf(n):
    v = [0,0]
    for i in n:v=b(i,v)
    return max(v)
if __name__ == '__main__':
    # These using only for self-checking and not necessary for auto-testing
    assert golf((5, -3, -1, 2)) == 6
    assert golf((5, 6, -10, -7, 4)) == 8
    assert golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
    assert golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125
