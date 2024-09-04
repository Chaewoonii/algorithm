#백준 2178, 미로탐색
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
around = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def findPath(graph, x = 0, y = 0):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i, j in around:
            nx = x + i
            ny = y + j

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
            else:
                continue

    return graph[n - 1][m - 1]

print(findPath(maze))