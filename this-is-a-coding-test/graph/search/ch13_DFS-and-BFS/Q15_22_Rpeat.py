import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
from utils.myutil import print_matrix

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

# 연구소
# 벽 3개 조합 -> 바이러스 퍼트리기 -> 안전영역 크기 구하기
# 바이러스가 안퍼짐.. 이유 찾기..
def laboratory():
    n, m = map(int, input().split())
    lab_map = [list(map(int, input().split())) for _ in range(n)]
    safe_area = [] # 안전 영역 정보
    virus_loc = [] # 바이러스 정보

    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0: safe_area.append((i, j))
            elif lab_map[i][j] == 2: virus_loc.append((i, j))
    walls = combinations(safe_area, 3) # 벽 3개 조합
    result = 0
    for combi in walls:
        temp_map = deepcopy(lab_map)
        # 벽 세우기
        for wx, wy in combi:
            temp_map[wx][wy] = 1

        # 바이러스 퍼뜨리기
        for v in virus_loc:
            temp_map = virus(temp_map, v)
            # mu.print_matrix(temp_map)

        # 최종 안전 영역의 개수 구하기
        result = max(result, getTargetCnt(temp_map, 0))

    return result

def virus(graph, start):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([start])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

    return graph

def getTargetCnt(graph, target):
    target_cnt = 0
    for li in graph:
        target_cnt += li.count(target)
    return target_cnt

# 경쟁적 전염
def competitive_contagion():
    n, k = map(int, input().split())
    test_tube = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())

    virus_location = []
    for i in range(n):
        for j in range(n):
            if test_tube[i][j] != 0:
                virus_location.append((test_tube[i][j], i, j)) # 바이러스 번호 순

    virus_location.sort(key=lambda x: x[0])
    time = 0
    while virus_location and time < s:
        time += 1
        virus_location = virusBFS(test_tube, virus_location)

    return test_tube[x - 1][y - 1]

def virusBFS(test_tube, virus_location):
    #    상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    new_location = []

    for _ in range(len(virus_location)):
        v, x, y = virus_location.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(test_tube) and 0 <= ny < len(test_tube):
                if test_tube[nx][ny] == 0:
                    test_tube[nx][ny] = v
                    new_location.append((v, nx, ny))
                    continue

    return new_location

if __name__ == "__main__":
    print(competitive_contagion())