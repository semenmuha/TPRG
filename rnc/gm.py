import math


def gm(p1, p2, p3, file_name):
    x = []
    with open(file_name) as f:
        for line in f:
            for a in line.split():
                x.append(int(a))
    res = []
    left_border = 1
    right_border = len(x)
    for i in range(left_border, right_border):
        u = []
        for j in range(p3):
            u.append(x[i - j] % 1024)
        u_mult = 1
        for j in range(len(u)):
            u_mult = u_mult * (1 - u[j])
        y = p1 - p2 * math.log1p(math.fabs(u_mult))
        y = format(y, '.4f')
        res.append(y)
    return res
