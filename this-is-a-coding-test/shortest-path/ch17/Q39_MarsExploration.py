# 388p, 화성 탐사

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())


for _ in range(n):
    m = int(input())
    graph = [list(map(int, input().split())) for _ in range(m)]
    distance = [INF] * m
    q = []
    heapq.heappush(q, (graph[0][0], 0))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist +