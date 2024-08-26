# 구현 실전문제 3, 게임 개발
# 북0, 동1, 남2, 서3
# 북-서-남-동-북

n, m = map(int, input().split())
row, col, direction = map(int, input().split())
gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

# 방문 정보
visit = [[0] * m for i in range(n)]

# 캐릭터의 이동, 북, 동, 남, 서
dRow = [-1, 0, 1, 0] # 세로, 북, 남 이동
dCol = [0, -1, 0, 1] # 가로, 동, 서 이동

# 처음 주어진 좌표 방문 처리
visit[row][col]= 1

# 방향 회전, 왼쪽으로
def turnLeft(d):
    if d == 0: d = 3
    else:
        d -= 1

    return d

# 앞으로 전진
def goForward(d, r, c):
    r += dRow[d]
    c += dCol[d]

    return r, c

# 뒤로 전진
def goBack(direction, r, c):
    r -= dRow[direction]
    c -= dCol[direction]

    return r, c

# 방문 체크
def checkVisit(r, c):
    cnt = 0
    if visit[r][c] == 0 and gameMap[r][c] == 0:
        visit[r][c] = 1
        cnt += 1

    return cnt

while True:
    direction = turnLeft(direction)
    row2, col2 = goForward(direction, row, col)
    cnt = checkVisit(row2, col2)
    if cnt:
        row, col = row2, col2
        continue
    else:
        row2, col2 = goBack(direction, row2, col2)
        if gameMap[row2][col2] == 0:
            row, col = row2, col2
        else:
            break



