# 388p, 화성 탐사

import heapq
import sys

input = sys.stdin.readline
INF = 1e9

    # 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for test in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)] # 거리, 좌표 x, 좌표 y | 시작위치
    distance[x][y] = graph[x][y]

    # 다익스트라
    while q:
        dist, x, y = heapq.heappop(q)

        # 방문 노드 무시
        if dist < distance[x][y]: continue

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # graph 범위 검증
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue

            # 해당 노드를 거쳐 다음 위치로 가기 위한 비용
            cost = dist + graph[nx][ny]

            # 해당 노드를 거쳐 가는 편이 비용이 더 작다면 업데이트, q에 삽입
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1]) # 정답 출력