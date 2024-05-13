from progress.bar import IncrementalBar


def lfsr(flag, n_, parameters_):
    if flag:
        bar = IncrementalBar('Выполнение:', max=n_)
    taps = []
    if parameters_[0]:
        for i, j in enumerate(str(parameters_[0])[::-1]):
            if j == '1':
                taps.append(i)
        state = int(parameters_[1])
        w = int(parameters_[2])
    else:
        for i, j in enumerate(str(101101010)[::-1]):
            if j == '1':
                taps.append(i)
        state = 541
        w = 10
    feedback = 0
    res = []
    for i in range(n_):
        x_bin = ''
        for j in range(w):
            for tap in taps:
                feedback ^= (state >> tap) & 1
            state = ((state << 1) | feedback) & ((1 << max(taps) + 1) - 1)
            x_bin += str(state >> 1 & 1)
        res.append((int(x_bin, 2)))
        if flag:
            bar.next()
    if flag:
        bar.finish()
    return res
