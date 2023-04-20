def bfs(graph, source, sink, parent):
    n = len(graph)
    visited = [False] * n
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

    return visited[sink]


graph = [
    [0, 7, 4, 0, 0, 0],
    [0, 0, 4, 0, 2, 0],
    [0, 0, 0, 4, 8, 0],
    [0, 0, 0, 0, 0, 12],
    [0, 0, 0, 4, 0, 5],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5

n = len(graph)
parent = [-1] * n
max_flow = 0

while bfs(graph, source, sink, parent):
    path_flow = float("Inf")
    s = sink

    while s != source:
        path_flow = min(path_flow, graph[parent[s]][s])
        s = parent[s]

    max_flow += path_flow

    v = sink
    while v != source:
        u = parent[v]
        graph[u][v] -= path_flow
        graph[v][u] += path_flow
        v = parent[v]



print(max_flow)