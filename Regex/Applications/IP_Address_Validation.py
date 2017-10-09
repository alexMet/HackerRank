import re

def gyrnaw(st):
    ret = re.match(r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])([.]([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){1,3}$", st)
    
    if ret:
        return "IPv4"
        
    ret = re.match(r"^[0-9a-f]{1,4}(:[0-9a-f]{1,4}){1,7}$", st)

    if ret:
        return "IPv6"
        
    return "Neither"

n = int(input())

for _ in range(0, n):
    print (gyrnaw(input()))
