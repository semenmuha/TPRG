from lfsr import lfsr


def nfsr(n_, parameters_):
    bar = IncrementalBar('Выполнение:', max=n_)
    result = []
    if parameters_[0]:
        w = parameters_[6]
        x1 = lfsr(False, n_, [parameters_[0], parameters_[3], w])
        x2 = lfsr(False, n_, [parameters_[1], parameters_[4], w])
        x3 = lfsr(False, n_, [parameters_[2], parameters_[5], w])
    else:
        w = 10
        x1 = lfsr(n_, [1010110101010, 541, w])
        x2 = lfsr(n_, [1010110101010, 993, w])
        x3 = lfsr(n_, [1010110101010, 117, w])
    for i in range(0, n_):
        x1Element = x1[i]
        x2Element = x2[i]
        x3Element = x3[i]
        resultTemp = (x1Element & x2Element) ^ (x2Element & x3Element) ^ x3Element
        result.append(resultTemp)
        bar.next()
    bar.finish()
    return result
