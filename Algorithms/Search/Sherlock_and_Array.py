def is_there(ar, n):
    suml = 0
    sumr = sum(ar) - ar[0]
    
    if suml == sumr:
        return True

    for i in range(1, n):
        suml += ar[i-1]
        sumr -= ar[i]
        
        if suml == sumr:
            return True
        
    return False
        
t = int(input())

for i in range(0, t):
    n = int(input())
    ar = list(map(int, input().split()))
    
    if is_there(ar, n):
        print ("YES")
    else:
        print ("NO")
