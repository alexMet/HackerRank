#!/bin/python3

import sys

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

print (len(word) * max([h[ord(i) - 97] for i in word]))
