# 깊이 우선 탐색 (DFS, Depth-First Search)
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘)
# 특정 경로로 탐색하다가 특정한 상황에서 최대한 깊이 들어가서 노드를 방문한 후 다시 돌아가 다른 경로로 탐색하는 알고리즘

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=' ') # 방문 노드 출력

    for i in graph[v]: # v 노드에 연결된 노드들을 차례로 탐색
        if not visited[i]: # 방문하지 않은 노드를
            dfs(graph, i, visited) # 재귀적으로 방문

# 그래프. 노드 0은 없으므로 비움, 노드 1~8의 연결된 노드 정보를 담음
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

# 방문 정보 저장
visited = [False] * len(graph)
dfs(graph, 1, visited)