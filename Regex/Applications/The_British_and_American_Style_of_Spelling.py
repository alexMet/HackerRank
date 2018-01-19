import re

def gyrna(us, n, line):
    uk = us[0:len(us)-2] + "s" + us[len(us)-1]
    
    cnt = 0
    for i in range(0, n):
        ret1 = re.findall(us, line[i])
        ret2 = re.findall(uk, line[i])

        cnt += len(ret1 + ret2)
            
    return cnt
    
lines = int(input())

a = [" "]*lines
for i in range(0, lines):
    a[i] = input()
    
t = int(input())
for _ in range(0, t):
    print (gyrna(input(), lines, a))
