import math


def ln(p1, p2, file_name):
    x = []
    with open(file_name) as f:
        for line in f:
            for a in line.split():
                x.append(int(a))
    res = []
    left_border = 0
    right_border = len(x)
    for i in range(left_border, right_border):
        u = x[i] % 1024
        y = math.exp(p2 - u) + p1
        y = format(y, '.4f')
        res.append(y)
    return res
