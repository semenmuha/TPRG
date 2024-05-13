import math


def nr(p1, p2, file_name):
    x = []
    with open(file_name) as f:
        for line in f:
            for a in line.split():
                x.append(int(a))
    res = []
    left_border = 0
    right_border = len(x)
    step = 2
    for i in range(left_border, right_border, step):
        u1 = x[i] % 1024
        u2 = x[i + 1] % 1024
        z1 = p1 + p2 * math.sqrt(math.fabs((-2) * math.log1p(math.fabs(1 - u1)))) * math.cos(2 * math.pi * u2)
        z2 = p1 + p2 * math.sqrt(math.fabs((-2) * math.log1p(math.fabs(1 - u1)))) * math.sin(2 * math.pi * u2)
        z1 = format(z1, '.4f')
        z2 = format(z2, '.4f')
        res.append(z1)
        res.append(z2)

    return res
