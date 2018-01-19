n = int(input())
a = [int(x) for x in input().split()]
h = [0] * 101

for i in a:
    h[i] += 1
    
print (n - max(h))
