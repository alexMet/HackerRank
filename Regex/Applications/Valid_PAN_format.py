import re
n = int(input())

for _ in range(0, n):
    ret = re.match(r"[A-Z]{5}[0-9]{4}[A-Z]$", input())
    
    if ret:
        print ("YES")
    else:
        print ("NO")
