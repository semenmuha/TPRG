def tr(p1, p2, file_name):
    x = []
    with open(file_name) as f:
        for line in f:
            for a in line.split():
                x.append(int(a))
    res = []
    left_border = 1
    right_border = len(x)
    for i in range(left_border, right_border):
        u1 = x[i - 1] % 1024
        u2 = x[i] % 1024
        y = p1 + p2 * (u1 + u2 - 1)
        y = format(y, '.4f')
        res.append(y)
    return res
