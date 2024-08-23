n, m = map(int, input().split())
x, y, direction = map(int, input().split())

visitedMap = [[0] * m for i in range(n)]
visitedMap[x][y] = 1

gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

# 북0, 동1, 남2, 서3 / 북-서-남-동-북
moveX = [-1, 0, 1, 0]
moveY = [0, 1, 0, -1]

def turnLeft(d):
    if d > 0:
        d -= 1
    else:
        d = 3

    return d

count = 1
turn = 0
while True:
    direction = turnLeft(direction)
    nx = x + moveX[direction]
    ny = y + moveY[direction]

    if visitedMap[nx][ny] == 0 and gameMap[nx][ny] == 0:
        x, y = nx, ny
        visitedMap[x][y] = 1
        count += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx = x - moveX[direction]
        ny = y - moveY[direction]

        if gameMap[nx][ny] == 0:
            x, y = nx, ny
        else:
            break

        turn = 0

print(count)
