def caric(n):
    div = n // 3
    mod = n % 3
    
    if n == 1 or n == 2:
        return "-1"
    
    if mod == 0:
        #print ("ena")
        return "5"*n
    
    left = div * 3
    right = mod
    
    for i in range(div, -1, -1):
        if right % 5 == 0:
            return "5"*left + "3"*right
        
        left = i * 3
        right = n - left
        
    if n % 5 == 0:
        return "3"*n
    
    return "-1"
    
t = int(input())

for _ in range(t):
    print (caric(int(input())))
