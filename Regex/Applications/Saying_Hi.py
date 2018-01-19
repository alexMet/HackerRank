import re

n = int(input())

for _ in range(0, n):
    st = input()
    ret = re.match(r"^hi [^dD]", st, re.IGNORECASE)
    
    if ret:
        print (st)
