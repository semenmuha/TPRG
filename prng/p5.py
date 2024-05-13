from progress.bar import IncrementalBar


def p5(n_, parameters_):
    bar = IncrementalBar('Выполнение:', max=n_)
    res = []
    if parameters_[0]:
        p, q1, q2, q3, w, key = int(parameters_[0]), int(parameters_[1]), int(parameters_[2]), int(parameters_[3]), \
                            int(parameters_[4]), str(parameters_[5])
    else:
        p, q1, q2, q3, w, key = 89, 20, 40, 69, 10, 12
    while len(key) < p:
        key = '0' + key
    counter = 0
    for i in range(n_):
        x_bin = ''
        for j in range(w):
            x = int(key[counter + q1]) + int(key[counter + q2]) + int(key[counter + q3]) + int(key[counter])
            counter += 1
            x = x % 2
            key += str(x)
            x_bin += str(x)
        res.append(int(x_bin, 2))
        bar.next()
    bar.finish()
    return res
