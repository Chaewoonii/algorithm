# 게임개발 연습

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

visitMap = [[0] * m for i in range(n)]


gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

    # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft(d):
    if d == 0:
        d = 3
    else:
        d -= 1

    return d

count = 0
turn = 0
visitMap[x][y] = 1
count += 1
while True:
    direction = turnLeft(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]
    if gameMap[nx][ny] == 0 and visitMap[nx][ny] == 0:
        visitMap[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn = 0
        continue

    else:
        turn += 1
        if turn == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if gameMap[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
                turn = 0
                continue

# print(visitMap)
print(count)

