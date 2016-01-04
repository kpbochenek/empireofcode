# kpbochenek@gmail.common

def ifcheck(number, result, val, res):
    if number >= val:
        return number - val, result + res
    return number, result


def whilecheck(number, result, val, res):
    while number >= val:
        number -= val
        result += res
    return number, result


def roman(number):
    result = ""
    number, result = whilecheck(number, result, 1000, 'M')
    number, result = ifcheck(number, result, 900, 'CM')
    number, result = ifcheck(number, result, 500, 'D')
    number, result = ifcheck(number, result, 400, 'CD')
    number, result = whilecheck(number, result, 100, 'C')
    number, result = ifcheck(number, result, 90, 'XC')
    number, result = ifcheck(number, result, 50, 'L')
    number, result = ifcheck(number, result, 40, 'XL')
    number, result = whilecheck(number, result, 10, 'X')
    number, result = ifcheck(number, result, 9, 'IX')
    number, result = ifcheck(number, result, 5, 'V')
    number, result = ifcheck(number, result, 4, 'IV')
    number, result = whilecheck(number, result, 1, 'I')
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("Earn cool rewards by using the 'Check' button!")
