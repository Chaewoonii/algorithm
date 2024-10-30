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
    visited[start] = 1 # 시작 노드 방문 처리
    print(start, end=' ')

    for node in graph[start]: #시작 노드의 인접 노드 방문
        if not visited[node]:
            dfs(graph, node, visited) # 재귀함수 호출(미방문 노드 방문 처리, 인접노드 방문)

visited1 = [0] * len(graph) # 재귀함수이기 때문에 방문 정보를 함수 밖에 저장 해야 함.
dfs(graph, 1, visited1)
print()

#bfs
def bfs(graph, start):
    queue = deque([start])
    visited = [0] * len(graph) # 재귀함수가 아니기 때문에 함수 안에서 방문 정보 저장 가능.
    visited[start] = 1 #시작 노드 방문 처리

    while queue: # 큐에 미방문 원소를 넣고 큐가 빌 때까지 반복 (=모든 노드를 방문할 때까지 반복한다)
        node = queue.popleft() #큐의 첫 번째 원소 꺼냄
        print(node, end=' ')

        for n in graph[node]: #꺼낸 첫 번째 원소의 인접노드 순차 방문
            if not visited[n]:
                queue.append(n)  # 방문하지 않았던 노드 방문 처리 및 큐 삽입.
                visited[n] = True

bfs(graph, 1)
