def read_input():
    n = int(input())
    m = int(input())
    dun = [''] * n
    
    for i in range(0, n):
        dun[i] = input().split()
            
    return n, m, dun
    
    
def do_the_dfs(n, m, dun, visited, start):
    path = [start]
    cnt = 0
    
    while path:
        x, y = path.pop()
            
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
            
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i < n) and (i >= 0) and (j < m) and (j >= 0) and (dun[i][j] == '1') and (not visited[i][j]):
                            path += [(i, j)]

                    #if (x != 0) and (dun[x-1][y] != 'X') and (not visited[x-1][y]):
                    #    path += [(x-1, y)]

                    #if (y+1 != m) and (dun[x][y+1] != 'X') and (not visited[x][y+1]):
                    #    path += [(x, y+1)]

                    #if (y != 0) and (dun[x][y-1] != 'X') and (not visited[x][y-1]):
                    #    path  += [(x, y-1)]
    return cnt

                
if __name__ == "__main__":
    n, m, dun = read_input()
    visited = [[False for _ in range(m)] for _ in range(n)]
    maxx = 0
    
    for i in range(n):
        for j in range(m):
            if dun[i][j] == '1' and not visited[i][j]:
                w = do_the_dfs(n, m, dun, visited, (i, j))
                maxx = w if w > maxx else maxx
    
    print (maxx)
