# kpbochenek@gmail.common


def test(game_result, v):
    vvv = v + v + v
    for r in game_result:
        if vvv in r:
            return True
    rgame = []
    for i in range(len(game_result[0])):
        rgame.append(''.join([t[i] for t in game_result]))
    for r in rgame:
        if vvv in r:
            return True
    if game_result[0][0] == v and game_result[1][1] == v and game_result[2][2] == v:
        return True
    if game_result[2][0] == v and game_result[1][1] == v and game_result[0][2] == v:
        return True
    return False


def xo_referee(game_result):
    xwin = test(game_result, "X")
    owin = test(game_result, "O")
    if (xwin and owin): return "D"
    if xwin: return "X"
    if owin: return "O"
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    # Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    print("Earn cool rewards by using the 'Check' button!")
