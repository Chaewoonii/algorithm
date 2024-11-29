# 353, 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque
from itertools import count

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(country, start):
    queue = deque([start])
    total = country[start[0]][start[1]]
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if L <= abs(country[x][y] - country[nx][ny]) <= R:
                total += country[nx][ny]
                count += 1