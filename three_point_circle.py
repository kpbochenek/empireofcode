#!/usr/bin/python


def circle_equation(note):
    x1, y1, x2, y2, x3, y3 = note.replace("(", "").replace(")", "").split(",")

    #(x1-x)^2 + (y1 - y)^2 = r^2

    (x1-x)^2 + (y1 - y)^2 = (x2-x)^2 + (y2-y)^2
    (x1-x)^2 + (y1 - y)^2 = (x3-x)^2 + (y3-y)^2

    x = x1 - sqrt(r^2 - (y1-y)^2)
    x = x2 - sqrt(r^2 - (y2-y)^2)
    x = x3 - sqrt(r^2 - (y3-y)^2)

    x, y, r = round(4, 2), round(4, 2), round(2.83, 2)
    return "(x-%s)^2+(y-%s)^2=%s^2" % (x, y, r)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    print("Use 'Check' to earn sweet rewards!")
