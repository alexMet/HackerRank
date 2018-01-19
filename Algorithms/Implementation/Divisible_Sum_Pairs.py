#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

cnt = 0
a.sort()
for i in range(0, n):
    for j in range(i + 1, n):
        if ((a[i] + a[j]) % k == 0):
            cnt += 1
print (cnt)
