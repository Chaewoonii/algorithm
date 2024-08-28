# 너비 우선 탐색(BFS, Breadth First Search)
# 가까운 노드부터 탐색하는 알고리즘
# 선입선출, 큐 이용

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 생성, 시작노드를 큐에 삽입
    visited[start] = True #현재 노드 방문 처리

    while queue: #큐가 빌 때까지 반복
        v = queue.popleft() #선입선출, 가장 먼저 삽입된 노드부터 탐색
        print(v, end=' ')
        for i in graph[v]: # v노드에 연결된 노드들 탐색
            if not visited[i]: # i노드 방문처리 안 되었을 경우
                queue.append(i) # 큐에 삽입
                visited[i] = True # 방문 처리

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

visited = [False] * len(graph)
bfs(graph, 1, visited) # 노드 1 부터 탐색 시작