#!/bin/python3

import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

#a = a[abs(n - k):] + a[:abs(n - k)]
l = len(a)
ind = (l - k) % l
a = a + a
a = a[ind:ind + l]

for a0 in range(q):
    m = int(input().strip())
    print (a[m])
