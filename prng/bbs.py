from progress.bar import IncrementalBar


def bbs(n_, parameters_):
    bar = IncrementalBar('Выполнение:', max=n_)
    res = []
    if parameters_[0]:
        x = int(parameters_[0])
    else:
        x = 7
    n, w = 50621, 10    #16637
    for i in range(n_):
        x_bin = ''
        for j in range(w):
            x = (x * x) % n
            x_bin += str(x % 2)
        res.append(int(x_bin, 2))
        bar.next()
    bar.finish()
    return res
