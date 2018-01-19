n, k = [int(x) for x in input().split()]
s = str(input())

ans = [s[0]]
acc = int(s[0])

for i in range(1, n):
    si = int(s[i])
    
    if i >= k:
        acc ^= int(ans[i - k]) 
    
    ai = acc ^ si
    acc ^= ai
    ans += str(ai)
    
print ("".join(ans))
