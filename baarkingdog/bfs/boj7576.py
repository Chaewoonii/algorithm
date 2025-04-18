from collections import deque

# 큐가 빌 때까지 토마토의 상하좌우 순회하며 큐에 넣고 값을 업데이트 한다.
def bfs(data, tomato):
    q = deque(tomato)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y] + 1
                    q.append((nx, ny))
    return data


def getResult(data):
    result = -1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                return -1
            result = max(result, data[i][j])
    return result - 1

# 실행부
M, N = map(int, input().split())
data = []
tomato = []
zero = 0
for i in range(N):
    row = list(map(int, input().split()))
    data.append(row)
    for j in range(M):
        if row[j] == 1: tomato.append((i, j))
        elif row[j] == 0: zero += 1

if zero == 0:
    print(0)
else:
    data = bfs(data, tomato)
    print(getResult(data))


