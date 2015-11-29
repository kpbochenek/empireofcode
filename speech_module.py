FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
LOW_TEN = FIRST_TEN + SECOND_TEN
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_small_number(number):
    result = []
    if number >= 100:
        ths = number // 100
        number = number % 100
        result.append(FIRST_TEN[ths])
        result.append(HUNDRED)
    if number > 0:
        if number < 20:
            result.append(LOW_TEN[number])
        else:
            result.append(OTHER_TENS[number // 10 - 2])
            number = number % 10
            if number is not 0:
                result.append(FIRST_TEN[number])
    return result


def tell_number(number):
    if number == 0: return FIRST_TEN[0]
    result = []
    if number < 0:
        result.append('minus')
        number = abs(number)

    if number >= 1000:
        result.extend(tell_small_number(number // 1000))
        result.append(THOUSAND)
        number = number % 1000
    result.extend(tell_small_number(number))

    print(result)
    return ' '.join(result)


if __name__ == '__main__':
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert tell_number(100) == 'one hundred', "hundred!"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")

