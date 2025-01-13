# 390p, 숨바꼭질

import heapq

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

INF = 1e9
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 연결된 간선의 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 최단거리 테이블
distance = [INF] * (n + 1)
distance[1] = 0 # 시작 위치 초기화
# 다익스트라 알고리즘 수행
q = [(0, 1)]
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for i in graph[now]:
        cost = dist + 1

        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

distance[0] = 0
print(distance.index(max(distance)), end=" ")
print(max(distance), end=" ")
print(distance.count(max(distance)))

