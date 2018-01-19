import re

n = int(input())

for _ in range(0, n):
    ret = re.match(r"[a-z]{0,3}[0-9]{2,8}[A-Z]{3}", input())
    
    if ret:
        print ("VALID")
    else:
        print ("INVALID")
