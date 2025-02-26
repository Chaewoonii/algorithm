N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, populations):
    union = [(x, y)]
    q = [(x, y)]
    visited[x][y] = True
    total = populations[x][y]
    cnt = 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False:
                if L <= abs(populations[x][y] - populations[nx][ny]) <= R:
                    union.append((nx, ny))
                    q.append((nx, ny))
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