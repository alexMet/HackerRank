t = int(input())

for _ in range(t):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    
    line = input().split()
    a = list(map(int, line))
    
    s = 0
    for i in a:
        if i <= 0:
            s += 1
    
    if s < k:
        print ("YES")
    else:
        print ("NO")
