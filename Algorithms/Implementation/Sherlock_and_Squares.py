import math

def vres_mia(a, b):
    
    sa = a ** 0.5
    while math.ceil(sa) != math.floor(sa):
        a += 1
        sa = a ** 0.5
    
    sb = b ** 0.5
    while math.ceil(sb) != math.floor(sb):
        b -= 1
        sb = b ** 0.5
        
    return int(sb - sa + 1)
    
t = int(input())

for _ in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    print (vres_mia(a, b))
