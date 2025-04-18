from collections import deque

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
drawings = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 1 and not visited[i][j]:
            drawings += 1
            size = 1
            q = deque([(i, j)])
            visited[i][j] = 1

            while q:
                x, y = q.popleft()

                for ni in range(4):
                    nx = x + dx[ni]
                    ny = y + dy[ni]

                    if 0 <= nx < N and 0 <= ny < M:
                        if not visited[nx][ny] and data[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                            size += 1

            result = max(result, size)

print(drawings)
print(result)
