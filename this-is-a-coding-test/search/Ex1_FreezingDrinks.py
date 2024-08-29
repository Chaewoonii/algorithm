# DFS/BFS 실전문제: 음료수 얼려 먹기

n, m = map(int, input().split())

iceFrame = []
for i in range(n):
    iceFrame.append(list(map(int, input())))

        # 상 하 좌 우
around = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfsAnswer(graph, x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        for i in around:  #얼음을 넣을 수 있다면 상하좌우 모두 재귀적으로 방문
            dfsAnswer(graph, x + i[0], y + i[1])

        return True # 연결된 0을 모두 방문했다면 True를 반환.

    return False

result = 0
#이중 반복문으로 전체 탐색.
for i in range(n):
    for j in range(m):
        if dfsAnswer(iceFrame, i, j): #얼음을 넣을 수 있고(0이고), 연결된 0을 모두 방문했다면
            result += 1 #카운트를 1 올림

print(result)

