from heapq import heappush, heappop

INF = 1e9

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares: # 그래프 구성
        graph[c].append((d, f))
        graph[d].append((c, f))

    # s, a, b에서 각 노드까지의 비용 계산
    dist_s = dijkstra(s, graph, n)
    dist_a = dijkstra(a, graph, n)
    dist_b = dijkstra(b, graph, n)

    # 최소비용 계산: s에서 m을 거쳐 a, b 로 가는 비용 중 최솟값
    total_cost = INF
    for m in range(1, n + 1):
        total_cost = min(total_cost, dist_s[m] + dist_a[m] + dist_b[m])
    return total_cost

def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            n_cost = dist + cost

            if n_cost < distance[node]:
                distance[node] = n_cost
                heappush(q, (n_cost, node))

    return distance

result = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(result)