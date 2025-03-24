# https://school.programmers.co.kr/learn/courses/30/lessons/49189

import heapq
INF = 1e9

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 다익스트라
    q = []
    heapq.heappush(q, (0, 1))  # 거리, 시작노드
    distance = [INF] * (n + 1)  # 최단거리 테이블
    distance[0] = distance[1] = 0  # 시작지점 초기화

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue  # 방문한 적 있다면 무시

        for node in graph[now]:  # 현재 노드와 연결된 노드들 탐색
            cost = dist + 1  # 방문비용 계산

            if cost < distance[node]:  # 방문 비용이 더 적다면
                distance[node] = cost  # 최단거리테이블 업데이트
                heapq.heappush(q, (cost, node))

    max_cost = max(distance)
    return sum(1 for i in range(n + 1) if distance[i] == max_cost)

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))