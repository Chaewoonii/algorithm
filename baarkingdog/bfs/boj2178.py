# 한 번 풀어봤던 문제
from collections import deque

N, M = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if data[i][j] > 0:
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                for ni in range(4):
                    nx = x + dx[ni]
                    ny = y + dy[ni]

                    if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 1:
                        q.append((nx, ny))
                        data[nx][ny] = data[x][y] + 1

for i in range(N):
    print(data[i])
print(data[N-1][M-1])