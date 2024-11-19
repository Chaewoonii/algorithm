# 344p, 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())
test_tube = []
virus = []

for i in range(n):
    test_tube.append(list(map(int, input().split())))

    for j in range(n):
        if test_tube[i][j] != 0:
            virus.append((test_tube[i][j], 0, i, j))

virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    v, s, x, y = q.popleft()
    if s == target_s: break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = v
                q.append((v, s + 1, nx, ny))

print(test_tube[target_x - 1][target_y - 1])