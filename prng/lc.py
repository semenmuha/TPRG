from progress.bar import IncrementalBar


def lc(n_, parameters_):
    bar = IncrementalBar('Выполнение:', max=n_)
    res = []
    if parameters_[0]:
        m, a, c, x = int(parameters_[0]), int(parameters_[1]), int(parameters_[2]), int(parameters_[3])
    else:
        m, a, c, x = 6075, 106, 1283, 7
    for i in range(n_):
        x = (a * x + c) % m
        res.append(x)
        bar.next()
    bar.finish()
    return res
