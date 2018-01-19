def read_input(dic, dist):  
    num = [int(i) for i in input().split()]
    
    for i in range(1, num[0]+1):
        dic[i] = []
        dist[i] = 0
        
    for i in range(0, num[1]):
        line = [int(i) for i in input().split()]
        dic[line[0]].append(line[1])
        dic[line[1]].append(line[0])
                   
    return int(input())

def do_the_bfs(dic, dist, s):
    que = [s]
    
    while que:
        cur = que.pop(0)
        child = dic[cur]
        curd = dist[cur]
        
        for i in child:
            if i != s and dist[i] == 0:
                dist[i] = curd + 6
                que.append(i)
    
    
def my_print(dic, dist, s):
    out = ""
    for i in dic.keys():
        if i != s:
            if dist[i] == 0:
                out += "-1 "
            else:
                out += str(dist[i]) + " "
    
    print (out)
                
n = int(input())

for i in range(0, n):
    dic = {}
    dist = {}
    s = read_input(dic, dist)
    do_the_bfs(dic, dist, s)
    my_print(dic, dist, s)
    
