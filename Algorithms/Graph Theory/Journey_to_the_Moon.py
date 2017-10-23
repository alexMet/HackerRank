def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

v, k = [int(i) for i in input().split()]
parent = []
rank = []

for node in range(v):
    parent.append(node)
    rank.append(0)

for edge in range(k):
    a, b = [int(i) for i in input().split()]
    x = find(parent, a)
    y = find(parent ,b)

    if x != y:
        union(parent, rank, x, y)

node = {}
for i in range(v):
    p = find(parent, i)

    try:
        node[p] += 1
    except KeyError:
        node[p] = 1

total = 0
for group, count in node.items():
    v -= count
    total += count * v

print (total)
