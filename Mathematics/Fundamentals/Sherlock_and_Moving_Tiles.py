from math import *

l, s1, s2 = [int(x) for x in input().split()]
n = int(input())

for i in range(n):
    q = int(input())
    print ("%.4f" % (sqrt(2) * abs((sqrt(q) - l)) / abs(s1 - s2)))
