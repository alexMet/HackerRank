import re

n = int(input())

for _ in range(0, n):
    ret = re.match(r"^[._][0-9]+[a-zA-Z]*[_]?$", input())
    
    if ret:
        print ("VALID")
    else:
        print ("INVALID")
