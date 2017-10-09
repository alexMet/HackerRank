for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    
    for i in range(n):
        times = (i + 1) * (n - i)
        
        if times & 1 == 1:
            ans ^= a[i]
            
    print (ans)
