# 최단경로 예제 복습

import sys
import heapq

input = sys.stdin.readline
INF = 1e9

# 37번 플로이드
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
def floyd():
    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())

        # 도시 a에서 b로 가는 노선은 하나가 아니며, 노선 중 최솟값을 저장하기 위한 조건
        if c < graph[a][b]: graph[a][b] = c

    # 자기 자신으로 가는 노선은 비용이 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b: graph[a][b] = 0
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF: print(0, end=" ")
            else: print(graph[i][j], end=" ")
        print()


# 38번, 정확한 순위
def exactRanking():
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b: graph[a][b] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = 0
    for a in range(1, n + 1):
        cnt = 0
        for b in range(1, n + 1):
            if graph[a][b] != INF or graph[b][a] != INF:
                cnt += 1

        if cnt == n: result += 1

    print(result)


# 39, 화성탐사
def marsExploration():
    for test in range(int(input())):
        n = int(input())
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        graph = [list(map(int, input().split())) for _ in range(n)]
        distance = [[INF] * n for _ in range(n)]

        x, y = 0, 0
        q = [(graph[x][y], x, y)]
        distance[x][y] = graph[x][y]

        while q:
            dist, x, y = heapq.heappop(q)

            if dist > distance[x][y]: continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue

                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

        print(distance[n-1][n-1])

# 40, 숨바꼭질
def hideAndSeek():
    n, m = map(int, input().split())
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    distance = [INF] * (n + 1)
    distance[1] = 0
    q = [(0, 1)] # 거리, 시작노드: 1번 노드에서 1번 노드로 가는 거리는 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + 1

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    for i in range(n + 1):
        if distance[i] == INF: distance[i] = 0

    print(distance.index(max(distance)), end=' ')
    print(max(distance), end=' ')
    print(distance.count(max(distance)), end=' ')

if __name__ == "__main__":
    hideAndSeek()