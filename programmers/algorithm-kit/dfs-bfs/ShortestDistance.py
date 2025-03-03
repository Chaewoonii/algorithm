from collections import deque

INF = 1e9

# bfs 문제 풀이
def solution(maps):
    answer = INF
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0, 1))
    while q:
        x, y, cnt = q.popleft()

        if x == N - 1 and y == M - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))

    return answer if answer != INF else -1