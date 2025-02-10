import sys
from collections import deque

input = sys.stdin.readline

# 특정 거리의 도시 찾기
def findCity():
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    distance = [-1] * (n + 1)
    distance[x] = 0
    q = deque([x])

    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

    reach = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            reach = True

    if not reach: print(-1)




if __name__ == "__main__":
    findCity()