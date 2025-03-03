# 353, 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, populations):
    union = [(x, y)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    total = populations[x][y]
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(populations[x][y] - populations[nx][ny]) <= R:
                    union.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    total += populations[nx][ny]
                    cnt += 1
    for i, j in union:
        populations[i][j] = total // cnt

result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    loc = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] is False:
                bfs(i, j, visited, populations)
                loc += 1
    if loc == N * N: break
    result += 1

print(result)


'''
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

p_cnt = 0
def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index 
    summary = graph[x][y] 
    count = 1 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    total_count += 1

print(total_count)
'''