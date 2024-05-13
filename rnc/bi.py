import math



def bi(p1, p2, file_name):
    x = []
    with open(file_name) as f:
        for line in f:
            for a in line.split():
                x.append(int(a))
    res = []
    left_border = 0
    right_border = len(x)
    for i in range(left_border, right_border):
        u = x[i] / 1024
        y = 0
        s = 0
        k = 0
        while (True):
            s = s + (math.factorial(p2) / (math.factorial(k) * math.factorial(p2 - k))) * (p1 ** k) *\
                ((1 - p1) ** (p2 - k))
            if s > u:
                y = k
                break
            if k < p2 - 1:
                k = k + 1
                continue
            y = p2
            break
        res.append(y)

    return res

