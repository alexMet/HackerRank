#!/bin/python3
import sys

s = input().strip()
print (len([i for i in s if i.isupper()]) + 1)
