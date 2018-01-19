#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    minDiff = abs(arr[0] - arr[1])
    for i in range(n - 1):
        curDiff = abs(arr[i] - arr[i + 1])
        if curDiff < minDiff: minDiff = curDiff
    return minDiff
    
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print (result)
