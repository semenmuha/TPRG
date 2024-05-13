from progress.bar import IncrementalBar


def add(n_, parameters_):
    bar = IncrementalBar('Выполнение:', max=n_)
    res = []
    if parameters_[0]:
        xs = list(int(i) for i in parameters_) + [31, 93, 35, 97, 35, 58, 85, 32, 93, 16, 61, 78, 46, 67, 5, 66, 5, 97, 9, 83, 30, 51, 85, 84,89, 30, 27, 53, 72, 32, 92, 13, 93, 5, 1, 97, 95, 24, 53, 28, 75, 4, 62, 4, 21, 75, 50, 6, 8, 3, 14, 62, 49, 95, 8]
    else:
        xs = [1024, 9, 49, 31, 93, 35, 97, 35, 58, 85, 32, 93, 16, 61, 78, 46, 67, 5, 66, 5, 97, 9, 83, 30, 51, 85, 84,
              89, 30, 27, 53, 72, 32, 92, 13, 93, 5, 1, 97, 95, 24, 53, 28, 75, 4, 62, 4, 21, 75, 50, 6, 8, 3, 14, 62,
              49, 95, 8]
    m = xs.pop(0)
    k = xs.pop(0)
    j = xs.pop(0)
    base_lan = len(xs)
    for n in range(base_lan, n_ + base_lan):
        x = (xs[n - k] + xs[n - j]) % m
        xs.append(x)
        res.append(x)
        bar.next()
    bar.finish()
    return res
