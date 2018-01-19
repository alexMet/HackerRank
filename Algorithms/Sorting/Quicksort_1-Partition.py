#!/bin/python

def partition(ar):
    left = ""
    right = ""
    for i in range(1, len(ar)):
        if ar[i] <= ar[0]:
            left += str(ar[i]) + " "
        if ar[i] > ar[0]:
            right += str(ar[i]) + " "
            
    return left + str(ar[0]) + " " + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)

