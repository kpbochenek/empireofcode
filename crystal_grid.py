# kpbochenek@gmail.com


def check_grid(grid):
    ly = len(grid)
    lx = len(grid[0])
    for x in range(lx):
        for y in range(ly):
            if x > 0 and grid[y][x-1] == grid[y][x]:
                return False
            if y > 0 and grid[y-1][x] == grid[y][x]:
                return False
            if x < lx-1 and grid[y][x+1] == grid[y][x]:
                return False
            if y < ly-1 and grid[y+1][x] == grid[y][x]:
                return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"
