# 플로이드워셜 알고리즘, 시간복잡도(O(N^3))
# a에서 b로 갈 때 k번 노드를 거쳐가는 비용 계산, k번 노드를 거쳐가는 경우의 값이 더 작다면 테이블 갱신
# DP에 속함, 점화식: D(ab) = min(D(ab), D(ak) + D(kb))

INF = int(1e9)

# 노드 및 간선의 개수 입력
n, m = map(int, input().split())

# 2차원 리스트 생성 및 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b: graph[a][b] = 0

# 간선의 정보 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드워셜 알고리즘 수행
# 점화식: D(ab) = min(D(ab), D(ak) + D(kb))
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])

# 수행결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF: print("INFINITY", end=" ")
        else: print(graph[a][b], end=" ")

