import re

def pame_ligo(st):
    ret = re.match(r"^hackerrank$", st)
    if ret:
        return 0
    
    ret = re.match(r"^hackerrank.*hackerrank$", st)
    if ret:
        return 0
    
    ret = re.match(r"^hackerrank.*", st)
    if ret:
        return 1
    
    ret = re.match(r".*hackerrank$", st)
    if ret:
        return 2
    
    return -1

n = int(input())

for _ in range(0, n):
    print (pame_ligo(input()))
        
