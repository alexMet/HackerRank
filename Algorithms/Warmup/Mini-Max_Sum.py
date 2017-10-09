#!/bin/python

import sys

a,b,c,d,e = input().strip().split(' ')
x = [int(a),int(b),int(c),int(d),int(e)]

s = sum(x)
maxx = 0
minn = s

for i in x:
    ss = s - i
    
    if (ss > maxx):
        maxx = ss
        
    if (ss < minn):
        minn = ss
        
print (minn, maxx)
