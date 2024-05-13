from progress.bar import IncrementalBar


def rsa(n_, parameters_):
    p, q, e, x, l = int(parameters_[0]), int(parameters_[1]), int(parameters_[2]), int(parameters_[3]),\
                    int(parameters_[4])
    res = []
    bar = IncrementalBar('Выполнение:', max=n_)
    n = p * q
    f = (p - 1) * (q - 1)
    for i in range(n_):
        counter = l - 1
        seqElem = 0
        for j in range(l):
            x = x ** e % n
            bit = x & 1
            seqElem = seqElem | (bit << counter)
            counter -= 1
        res.append(seqElem)
        bar.next()
    bar.finish()
    return res
