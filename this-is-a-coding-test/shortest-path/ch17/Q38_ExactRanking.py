# 386p, 정확한 순위
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b: graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 도달 가능한지 체크. 자기 자신(0)은 도달 가능하다고 보고,
# 도달할 수 있는 회선(INF가 아닌)이 n개이면 자신의 정확한 위치를 알 수 있으므로, +1
result = 0
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1

    if count == n:
        result += 1

print(result)