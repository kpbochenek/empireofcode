# kpbochenek@gmail.com
import time

memo = ["A0"] + [chr(a) + str(b) for a in range(ord('A'), ord('Z')+1) for b in range(1, 10)]
dformat = "%Y-%m-%d"


def count_ingots(report):
    return sum(map(lambda v: memo.index(v), report.split(",")))


def count_reports(full_report, from_date, to_date):
    from_date, to_date = time.strptime(from_date, dformat), time.strptime(to_date, dformat)
    result = 0
    for line in full_report.split('\n'):
        data, ingots = line.split(' ')
        pdata = time.strptime(data, dformat)
        if from_date <= pdata and pdata <= to_date:
            result += sum([count_ingots(x) for x in ingots.split(",")])
    return result


if __name__ == '__main__':
    # These using only for self-checking and not necessary for auto-testing
    assert count_reports("2015-01-01 A1,B2\n"
                         "2015-01-05 C3,C2,C1\n"
                         "2015-02-01 B4\n"
                         "2015-01-03 Z9,Z9",
                         "2015-01-01", "2015-01-31") == 540, "Normal"
    assert count_reports("2000-02-02 Z2,Z1\n"
                         "2000-02-01 Z2,Z1\n"
                         "2000-02-03 Z2,Z1",
                         "2000-02-04", "2000-02-28") == 0, "Zero"
    assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"
