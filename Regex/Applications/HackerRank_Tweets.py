import re
n = int(input())
cnt = 0

for _ in range(0, n):
    ret = re.search(r"hackerrank", input(), re.IGNORECASE)
    
    if ret:
        cnt += 1
        
print (cnt)
