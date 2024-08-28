from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]



#DFS
def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

visited1 = [0] * len(graph)
dfs(graph, 1, visited1)

#bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for n in graph[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True

print()
visited2 = [0] * len(graph)
bfs(graph, 1, visited2)
