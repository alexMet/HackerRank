#!/bin/python3

import math


def read_input():
    xs = []
    ys = []
    f = open('trainingdata.txt', 'r')
    for line in f:
        x, y = list(map(float, line.split(',')))
        if y < 8.0:
            xs += [x]
            ys += [y]
    f.close()
    return xs, ys

def median(arr):
    m = sum(arr) / len(arr)
    return round(m, 2)

def standard_deviation(arr, m):
    s = sum(map(lambda x: (x - m) ** 2, arr)) / (len(arr) - 1)
    s = math.sqrt(s)
    return round(s, 3)

def correlation(xs, x_m, ys, y_m):
    a = 0
    for i in range(len(xs)):
      a += (xs[i] - x_m) * (ys[i] - y_m)
    x_2 = sum(map(lambda x: (x - x_m) ** 2, xs))
    y_2 = sum(map(lambda y: (y - y_m) ** 2, ys))
    b = math.sqrt(x_2 * y_2)
    return round(a / b, 3)

def train(xs, ys):
    m_x = median(xs)
    m_y = median(ys)
    s_x = standard_deviation(xs, m_x)
    s_y = standard_deviation(ys, m_y)
    r = correlation(xs, m_x, ys, m_y)
    b = round(r * s_y / s_x, 3)
    A = round(m_y - (b * m_x), 3)
    return b, A

if __name__ == '__main__':
    timeCharged = float(input())
    b, A = train(*read_input())
    timeLasting = round((b * timeCharged) + A, 2)
    print(min(timeLasting, 8))

