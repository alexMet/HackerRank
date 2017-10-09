def read_input():
    n, m = [int(i) for i in input().split()]
    dun = [''] * n
    start = end = (-1, -1)
    s = e = -1
    
    for i in range(0, n):
        dun[i] = input()

        s = dun[i].find('M')
        e = dun[i].find('*')
                
        if s != -1:
            start = (i, s)
        
        if e != -1:
            end = (i, e)
            
    k = int(input())
    return n, m, dun, k, start, end
    
    
def do_the_dfs(n, m, dun, start, end):
    path = [[start, 0]]
    visited = [[False for _ in range(m)] for _ in range(n)]
        
    while path:
        cur = path.pop()
        x, y = cur[0]
        w = cur[1]
        
        if (x, y) == end:
            return w
            
        if not visited[x][y]:
            visited[x][y] = True
            cnt = 0
            p = []
            
            if (x+1 != n) and (dun[x+1][y] != 'X') and (not visited[x+1][y]):
                p += [(x+1, y)]
                cnt += 1

            if (x != 0) and (dun[x-1][y] != 'X') and (not visited[x-1][y]):
                p += [(x-1, y)]
                cnt += 1

            if (y+1 != m) and (dun[x][y+1] != 'X') and (not visited[x][y+1]):
                p += [(x, y+1)]
                cnt += 1

            if (y != 0) and (dun[x][y-1] != 'X') and (not visited[x][y-1]):
                p  += [(x, y-1)]
                cnt += 1
    
            newW = (w + 1) if cnt > 1 else w
            for i in p:
                path += [[i, newW]]

                
if __name__ == "__main__":
    t = int(input())

    for i in range(0, t):
        n, m, dun, k, start, end = read_input()
        w = do_the_dfs(n, m, dun, start, end)
    
        print ("Impressed" if w == k else "Oops!")
    
