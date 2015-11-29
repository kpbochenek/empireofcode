# kpbochenek@gmail.com


check = lambda state, pos: all([state[i] == 1 for i in pos])


def rotate(state, pos):
    if check(state, pos): result = [0]
    else: result = []
    for i in range(len(state)-1):
        state = [state[-1]] + state[:-1]
        if check(state, pos):
            result.append(i+1)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
