#kpbochenek@gmail.com

def go_left(nr, mapa, destroyed):
    if (nr, nr-1) in mapa and nr-1 not in destroyed: return nr-1
    else: return -1
def go_right(nr, mapa, destroyed):
    if (nr, nr+1) in mapa and nr+1 not in destroyed: return nr+1
    else: return -1
def go_top(nr, mapa, dim, destroyed):
    if (nr, nr-dim) in mapa and nr-dim not in destroyed: return nr-dim
    else: return -1
def go_bottom(nr, mapa, dim, destroyed):
    if (nr, nr+dim) in mapa and nr+dim not in destroyed: return nr+dim
    else: return -1

def square_exists(nr, dim, mapa, size, destroyed):
    for i in range(dim): nr = go_right(nr, mapa, destroyed)
    for i in range(dim): nr = go_bottom(nr, mapa, size, destroyed)
    for i in range(dim): nr = go_left(nr, mapa, destroyed)
    for i in range(dim): nr = go_top(nr, mapa, size, destroyed)
    return nr != -1

def count_squares(*lines):
    mapa = set()
    destroyed = set()
    size = 4
    for l in lines:
        if max(l[0], l[1]) > 16: size = 5
        if l[0] == 0: destroyed.add(l[1]-1)
        elif l[1] == 0: destroyed.add(l[0]-1)
        else:
            mapa.add((l[0]-1, l[1]-1))
            mapa.add((l[1]-1, l[0]-1))
    result = 0
    for d in range(size+1):
        for nr in range(size*size):
            if square_exists(nr, d+1, mapa, size, destroyed):
                result += 1
    return result

if __name__ == '__main__':
    # Rank 1
    assert (count_squares([1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                          [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                          [10, 14], [12, 16], [14, 15], [15, 16]) == 3), "First, from description"
    assert (count_squares([1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                          [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                          [9, 13], [10, 11], [12, 16], [13, 14], [14, 15],
                          [15, 16]) == 2), "Second, from description"
    assert (count_squares([1, 2], [1, 5], [2, 6], [5, 6]) == 1), "Third, one small square"
    assert (count_squares([1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                          [9, 10]) == 0), "Fourth, it's not square"
    assert (count_squares([16, 15], [16, 12], [15, 11], [11, 10],
                          [10, 14], [14, 13], [13, 9]) == 0), "Fifth, snake"

    # Rank 2
    assert (count_squares([1, 2], [2, 7], [7, 6], [6, 1], [25, 24],
                          [24, 19], [19, 20], [20, 25]) == 2), "25"
    # Rank 3
    assert (count_squares([1, 2], [2, 7], [7, 6], [6, 1], [25, 24], [24, 19], [19, 20], [20, 25],
                          [6, 11], [0, 19], [10, 0], [11, 16], [16, 21], [21, 22], [22, 23],
                          [23, 24], [20, 15], [15, 10], [10, 5],
                          [5, 4], [4, 3], [3, 2]) == 1), "With zeroes"
    assert (count_squares([1, 2], [1, 5], [2, 6], [5, 6], [6, 0]) == 0), "Fail"
