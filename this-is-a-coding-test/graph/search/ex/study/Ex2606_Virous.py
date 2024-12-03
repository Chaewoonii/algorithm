#백준 2606, 바이러스
n = int(input())
m = int(input())

connected = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for i, j in connected:
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n+1)

def dfs(graph, start, visited):
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)

    return visited

answer = sum(dfs(graph, 1, visited)) - 1
print(answer)
