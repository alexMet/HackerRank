def dijkstra(start, nodes, distances):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue

            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance

        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break

        candidates = [node for node in unvisited.items() if node[1]]
        if not candidates: break

        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    for key, _ in unvisited.items():
        visited[key] = -1

    return visited

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        nodes = []
        distances = {}

        v, e = map(int, input().split(' '))
        for i in range(v):
            nodes += [i + 1]
            distances[i + 1] = {}

        for i in range(e):
            a, b, cost = map(int, input().split(' '))

            try:
                old_cost = distances[a][b]
                distances[a][b] = min(old_cost, cost)
            except KeyError:
                distances[a][b] = cost

            try:
                old_cost = distances[b][a]
                distances[b][a] = min(old_cost, cost)
            except KeyError:
                distances[b][a] = cost

        s = int(input())
        d = dijkstra(s, nodes, distances)

        for node, cost in list(d.items()):
            if node != s:
                print (cost, end=" ")
        print ()
