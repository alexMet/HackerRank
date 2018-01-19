#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

nums = [0] * 101
for i in c:
    nums[i] += 1

cnt = 0
for i in nums:
    cnt += i // 2
        
print (cnt)
        
