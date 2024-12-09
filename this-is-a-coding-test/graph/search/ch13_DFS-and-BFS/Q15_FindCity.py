# 339p, 특정 거리에서 도시 찾기
# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            queue.append(i)

check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)