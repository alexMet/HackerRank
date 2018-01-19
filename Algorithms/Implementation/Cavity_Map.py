n = int(input())

g = [0]*n
g2 = [0]*n
for i in range(n):
    line = input()
    g[i] = [0]*n
    g2[i] = [0]*n
    
    for j in range(n):
        g[i][j] = int(line[j])
        g2[i][j] = int(line[j])
    
for i in range(1, n-1):
    for j in range(1, n-1):
        cur = g[i][j]
        if g[i-1][j] < cur and g[i][j-1] < cur and g[i][j+1] < cur and g[i+1][j] < cur:
            g2[i][j] = "X"
            
for i in range(n):
    print ("".join(list(map(str, g2[i]))))
