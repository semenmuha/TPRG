from progress.bar import IncrementalBar


def rc4(n_, parameters_):
    res = []
    bar = IncrementalBar('Выполнение:', max=n_)
    length = 256
    if parameters_[0]:
        secretKey = parameters_
    else:
        secretKey = ['1', '2', '3', '4', '5', '6', '7', '31', '48', '178', '46', '91', '30', '15', '132', '154', '108',
                     '222', '245', '211', '103']
    sBox = [0] * length
    key = [0] * length
    for i in range(length):
        sBox[i] = i
    for i in range(length):
        key[i] = int(secretKey[i % len(secretKey)])
    j = 0
    for i in range(length):
        j = (j + sBox[i] + key[i]) % length
        sBox[i], sBox[j] = sBox[j], sBox[i]
    j = 0
    for i in range(n_, 0, -1):
        i = (i + 1) % length
        j = (j + sBox[i]) % length
        sBox[i], sBox[j] = sBox[j], sBox[i]
        t = (sBox[i] + sBox[j]) % length
        res.append(sBox[t])
        bar.next()
    bar.finish()
    return res
