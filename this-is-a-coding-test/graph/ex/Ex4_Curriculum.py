# 303p, 커리큘럼

from collections import deque
import copy


n = int(input())
indegree = [0] * (n + 1)
times = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    times[i] = info[0]
    for j in info[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topologySort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0: q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result
print(topologySort())