'''위상 정렬
- 순서가 정해진 일련의 작업을 차례대로 수행해야 할 때 사용
- 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
- 진입차수: 특정한 노드로 들어오는 간선의 개수

**동작 과정**
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복
  1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
  2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
'''

from collections import deque

# 노드와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수, 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초깋화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []  # 위상 정렬 수행 결과
    q = deque()

    # 첫 시작 시 진입차수가 0인 노드(시작 노드)를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐가 빌 때까지 반복
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    return result

print(topology_sort())
