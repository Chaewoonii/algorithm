import heapq as hq
INF = 1e9

# 노드 1번에서 2번 노드로 가는 비용은 10
# graph: [[(2, 10), (4, 3)], [(),()]]
def dijkstra(start, graph):
    q = [(0, start)]
    distance = [INF] * (len(graph) + 1)
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            new_dist = dist + cost

            if new_dist < distance[node]:
                distance[node] = new_dist
                hq.heappush((new_dist, node))

    return distance