t = int(input())

for i in range(t):
    # h = [x for x in range(n)]
    n, m, s = [int(x) for x in input().split()]
    
    ans = (((m % n) + (s - 1)) % n)
    if ans == 0:
        print (n)
    else: 
        print (ans)
