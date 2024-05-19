import math
import random
from sys import argv

n = 10000
pre = []
math_ozid = 0


def toFixed(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0' * (n-len(b)))


i = 0
file2 = open('generator.txt', 'w')
file3 = open('new_generator.txt', 'w')
while i < n:
    x = random.uniform(0.0, 1.0)
    y = random.randint(1000, 100000)
    if (y < 10000):
        y = str('0' + str(y))
    file2.write(str(toFixed(x, 3)) + '\n')
    file3.write(str(y) + '\n')
    i = i + 1
file2.close()
file3.close()


def variance(arr, math, n):
     d = 0
     for i in arr:
        d = ((i - math) ** 2) + d
     d = d / (n - 1)
     return d


def gen(fn):
     f = open(fn, "r")
     rez = []
     for line in f:
        rez.append(float(line))
     f.close()
     return rez


def hi_2(x, n):
     min_v = 0
     max_v = 0
     for i in x:
        if i < 0.5:
            min_v += 1
        else:
            max_v += 1
     s = round((((min_v - n/2) ** 2) / (n/2)) + ((max_v - n/2) ** 2 / (n/2)), 3)
     return s


def series(x):
     x = sorted(x)
     n = len(x)
     value_1 = 0
     value_2 = 0
     value_3 = 0
     value_4 = 0
     for i in range(n - 1):
        val1 = x[i]
        val2 = x[i + 1]
        if ((val1 > 0) and (val1 < 1/4)) and ((val2 > 0) and (val2 < 1/4)):
            value_1 = value_1 + 1
        elif ((val1 > 1/4) and (val1 < 2/4)) and ((val2 > 1/4) and (val2 < 2/4)):
            value_2 = value_2 + 1
        elif ((val1 > 2/4) and (val1 < 3/4)) and ((val2 > 2/4) and (val2 < 3/4)):
            value_3 = value_3 + 1
        elif ((val1 > 3/4) and (val1 < 1)) and ((val2 > 3/4) and (val2 < 1)):
            value_4 = value_4 + 1
     kol = n / 4
     res = round((((value_1 - kol) ** 2) / kol) + (((value_2 - kol) ** 2) / kol) + (((value_3 - kol) ** 2) / kol) +
                 (((value_4 - kol) ** 2) / kol), 3)
     return res


def interval(x):
     t = 2
     count = [0, 0, 0]
     r = 0
     kol = 0
     for i in x:
        if i < 0.2 and i > 0 or i > 0.6 and i < 1:
             r = r + 1
        if i > 0.2 and i < 0.6:
            if (r >= t):
                count[t] = count[t] + 1
                r = 0
            else:
                count[r] = count[r] + 1
                r = 0
     for i in count:
        kol += i
     p1 = kol * 0.4
     p2 = kol * 0.24
     p3 = kol * 0.36
     res = round((((count[0] - p1) ** 2) / p1) + (((count[1] - p2) ** 2) / p2) + (((count[2] - p3) ** 2) / p3), 3)
     return res


def preobr(x):
     rez = []
     razn_1 = 0
     d_same = 0
     t_same = 0
     for i in range(len(x)):
        p = x[i]
        if p == '0':
            p = "100"
        if (p[0] != p[1]) and (p[0] != p[2]) and (p[1] != p[2]):
            razn_1 += 1
        elif ((p[0] == p[1]) and (p[0] != p[2])) or ((p[0] == p[2]) and (p[0] != p[1])) or ((p[1] == p[2]) and (p[0] != p[1])):
            d_same += 1
        elif (p[0] == p[1]) and (p[0] == p[2]) and (p[1] == p[2]):
            t_same += 1
     rez.append(razn_1)
     rez.append(d_same)
     rez.append(t_same)
     return rez


def lef_chi(x, n):
     s = 0
     kol1 = 0.72 * n
     kol2 = 0.27 * n
     kol3 = 0.01 * n
     tmp1 = (x[0] - kol1) ** 2
     tmp2 = (x[1] - kol2) ** 2
     tmp3 = (x[2] - kol3) ** 2
     s = (tmp1 / kol1) + (tmp2 / kol2) + (tmp3 / kol3)
     return s


def split(x):
     x_value = []
     for i in x:
        tmp = str(int(i * 1000))
        if len(tmp) == 2:
            tmp = tmp + 'a'
        elif len(tmp) == 1:
            tmp = tmp + 'ab'
        x_value.append(tmp)
     p_p = preobr(x_value)
     n = len(x_value)
     kol1 = 0.72 * n
     kol2 = 0.27 * n
     kol3 = 0.01 * n
     rez = round((((p_p[0] - kol1) ** 2) / kol1) + (((p_p[1] - kol2) ** 2) / kol2) + (((p_p[2] - kol3) ** 2) / kol3), 3)
     return rez


def reshuffle(x):
     n = len(x)
     value_1 = 0
     value_2 = 0
     for i in range(n - 1):
        val1 = x[i]
        val2 = x[i + 1]
        if (val1 < 0.5) and (val2 < 0.5):
            value_1 += 1
        if (val1 > 0.5) and (val2 > 0.5):
            value_2 += 1
     count = n / 4
     rez = round((((value_1 - count) ** 2) / count) + (((value_2 - count) ** 2) / count), 3)
     return rez


def monoton(x):
     t = 2
     r = 0
     summa = 0
     count = [0, 0, 0]
     for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            r = r + 1
        if x[i] > x[i + 1]:
            i = i + 1
            if r >= t + 1:
                count[t] = count[t] + 1
                r = 1
            else:
                count[r - 1] = count[r - 1] + 1
                r = 1
     for i in count:
         summa += + i
     value1 = summa * 0.34
     value2 = summa * 0.40
     value3 = summa * 0.26
     rez = round(((((count[0] - value1) ** 2) / value1) + (((count[1] - value2) ** 2) / value2) +
                  ((count[2] - value3) ** 2 / value3)) / 10, 3)
     return rez


def conflict():
     n = 10000
     m = n * 10
     f = open("new_generator.txt", "r")
     x = []
     for line in f:
        x.append(int(line))
     f.close()
     teor_conflict = (n ** 2) / (2 * m)
     pre = set(x)
     count_confict = len(x) - len(pre)
     count = n - teor_conflict
     rez = ((((count_confict - teor_conflict) ** 2) / teor_conflict) + (((len(pre) - count) ** 2) / count)) / 100
     return rez


def statistic(x_):
    n = len(x_)
    math_ozid = 0
    arr_m = []
    arr_q = []
    arr_n = []
    for key in x_:
        math_ozid += key
    math_ozid = math_ozid / len(x_)
    math_ozid = round(math_ozid, 3)
    q_otklon = math.sqrt(variance(x_, math_ozid, len(x_)))
    q_otklon = round(q_otklon, 3)
    arr_m.append(math_ozid)
    arr_q.append(q_otklon)
    arr_n.append(n)
    m1 = arr_m[0]
    q1 = arr_q[0]
    print("Мат.ожидание = " + str(m1))
    print("Среднеквадратичное отклонение = " + str(q1))
    pogreshnost_m = (math.fabs(m1 - 0.5)) / m1
    pogreshnost_q = (math.fabs(q1 - (math.sqrt(1 / 12)))) / q1
    pogreshnost_m = round(pogreshnost_m, 3)
    pogreshnost_q = round(pogreshnost_q, 3)
    print("Погрешность для мат.ожидания в % = " + str(100 * pogreshnost_m))
    print("Погрешность для среднеквадратичного отклонения в % = " + str(100 * pogreshnost_q))


arg = list(i.split(':') for i in argv)
parameters = {'/g': 'help'}
if len(arg[1]) > 1:
    for i in arg[1::]:
        parameters[i[0]] = i[1]
match parameters['/g']:
        case 'lc':
            x = gen("generator_lc.txt")
        case 'add':
            x = gen("generator_add.txt")
        case '5p':
            x = gen("generator_5p.txt")
        case 'lfsr':
            x = gen("generator_lfsr.txt")
        case 'nfsr':
            x = gen("generator_nfsr.txt")
        case 'mt':
            x = gen("generator_mt.txt")
        case 'rc4':
            x = gen("generator_rc4.txt")
        case 'rsa':
            x = gen("generator_rsa.txt")
        case 'bbs':
            x = gen("generator_bbs.txt")
        case _:
            x = gen("generator.txt")

statistic(x)

#Мат.ожидание
for key in x:
    math_ozid += key
math_ozid = math_ozid / len(x)
math_ozid = round(math_ozid, 3)

#Критерий Хи-Квадрат
hi = hi_2(x, len(x))
if hi > 0.0158 and hi < 3.8415:
    print("Критерий Хи-квадрат подтвержден и он равен " + str(hi))
else:
    print("Критерий Хи-квадрат не подтвержден и он равен " + str(hi))

#Критерий Серий
series = series(x)
if series > 0.5844 and series < 7.8147:
    print("Критерий Cерий подтвержден и оно равен " + str(series))
else:
    print("Критерий Cерий не подтвержден и оно равен " + str(series))

#Критерий Интервалов
interval = interval(x)
if interval > 0.5844 and interval < 7.8147:
    print("Критерий Интервалов подтвержден и он равен " + str(interval))
else:
    print("Критерий Интервалов не подтвержден и он равен " + str(interval))

#Критерий Разбиений
razbien = split(x)
if razbien > 0.2107 and razbien< 5.9915:
    print("Критерий Разбиений подтвержден и он равен " + str(razbien))
else:
    print("Критерий Разбиений не подтвержден и он равен " + str(razbien))

#Критерий Перестановок
permut = reshuffle(x)
if permut > 0.0158 and permut< 3.8415:
    print("Критерий Перестановок подтвержден и он равен " + str(permut))
else:
    print("Критерий Перестановок не подтвержден и он равен " + str(permut))

#Критерий Монотонности
mono = monoton(x)
if mono > 0.2107 and mono < 5.9915:
    print("Критерий Монотонности подтвержден и он равен " + str(mono))
else:
    print("Критерий Монотонности не подтвержден и он равен " + str(mono))

#Критерий Конфликтов
confl = conflict()
if confl > 0.0158 and confl < 3.8415:
    print("Критерий Кофликтов подтвержден и он равен " + str(confl))
else:
    print("Критерий Конфликтов не подтвержден и он равен " + str(confl))


