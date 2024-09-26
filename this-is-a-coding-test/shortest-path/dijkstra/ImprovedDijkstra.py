# 개선된 다익스트라: 우선순위 큐를 이용
# 방문 여부 정보를 담는 리스트가 별도로 필요하지 않음(visited x)
# 거리를 기준으로 우선순위 큐에 담기기 때문에 최소값을 가지는 노드를 찾는 함수가 별도로 필요하지 않음.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 및 간선의 개수
n, m = map(int, input().split())
start = int(input()) # 시작 노드
graph = [[] for _ in range(n + 1)] # 노드 및 간선 정보
distance = [INF] * (n + 1) # 최단거리 테이블

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c) # a 노드에서 b 노드로 가는 비용은 c

# 우선순위 큐를 이용한 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)-> 첫 번째 원소인 거리를 기준으로 큐에 삽입
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 큐의 제일 위 원소(거리가 가장 짧은 원소)를 꺼냄

        # 현재 노드가 이미 처리된(최단거리 값이 고정된, 방문한 적이 있는) 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐 가는 것이 더 짧은 경우: 최단거리 테이블 초기화, 우선순위 큐 삽입.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])
