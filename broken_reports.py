def golf(b):return sum([(ord(z)-65)*9+int(x)for z,x in zip(b[:-1],b[1:])if '@'<z<'['and'0'<x<':'])

if __name__ == '__main__':
    # These using only for self-checking and not necessary for auto-testing
    assert golf("ASDA1,BB22D01C1") == 31
    assert golf("B1,C2,D3") == 60
    assert golf("DauLhM4IU8oVBoSznrFIWhIwsNLIDFIMbQBaAYLZlXYlLyZSSwqo79nYcfIbeiqiGlxIV,SOhZ6BDiChE9vgyN") == 576
