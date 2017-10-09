#!/bin/python3
import sys

s = input().strip()
n = int(input().strip())

lenS = len(s)
cnt = len([x for x in s if x == 'a'])

print (cnt * (n // lenS) + len([x for x in s[:(n % lenS)] if x == 'a']))
