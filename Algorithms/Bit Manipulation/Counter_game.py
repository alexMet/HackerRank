import math

def vres(n):
    k = 0
    
    while n != 1:
        if n & (n-1):
            n = n - 2**int(math.ceil(math.log(n, 2))-1)
            k += 1
        else:
            k += int(math.log(n, 2))
            break
        
    if k % 2 != 0:
        return "Louise"
    else:
        return "Richard"
            
t = int(input())

for _ in range(0, t):
    l = vres(int(input()))
    print (l)
    
