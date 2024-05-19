import matplotlib.pyplot as plt
import math


def mat(arr):
    m = 0
    for i in arr:
        m = m + i
    m = m / len(arr)
    return m


def disp(arr, mat):
    d = 0
    for i in arr:
        d = d + ((i - mat) ** 2)
    d = d / (len(arr) - 1)
    return d


f = open("generator.txt", "r")
input = []
arr_m = []
arr_d = []
arr_n = []
i = 0
for line in f:
    l = line.split(" ")
    for a in l:
        input.append(float(a))
        if (len(input) % 50 == 0):
            m = mat(input)
            d = math.sqrt(disp(input, m))
            i = i + 50
            arr_m.append(round(m, 3))
            arr_d.append(round(d, 3))
            arr_n.append(i)
fig = plt.figure()
for i in range(len(arr_n)):
    plt.scatter(arr_n[i], arr_m[i], c = 'b', s = 1)
plt.show()
for i in range(len(arr_n)):
    plt.scatter(arr_n[i], arr_d[i], c = 'b', s = 1)
plt.show()
