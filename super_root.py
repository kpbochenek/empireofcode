# kpbochenek@gmail.com

def super_root(number):
    minx, maxx = 0, 10
    while True:
        avg = (minx + maxx) / 2
        p = avg ** avg
        if number - 0.001 < p < number + 0.001:
            return avg
        elif p > number:
            maxx = avg
        else:
            minx = avg



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
