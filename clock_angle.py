def clock_angle(time):
    h, m = list(map(int, time.split(":")))

    if h > 12: h = h - 12

    h = h*30 + ((m/60)*30)
    m = (m)/60*360
    angle = abs(m - h)

    if angle >  180: angle = 360 - angle
    if angle == 0.0: return 0

    s = str(format(angle, '.1f'))
    if '.' in s:
        return float(s)
    else:
        return int(s)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
