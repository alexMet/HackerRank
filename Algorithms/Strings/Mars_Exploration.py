#!/bin/python3
import sys

S = input().strip()
word = "SOS"
ind = 0
cnt = 0

for i in S:
    if word[ind] != i:
        cnt += 1

    ind = (ind + 1) % 3

print (cnt)
