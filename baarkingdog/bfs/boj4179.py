# 불!
# 큐에 지훈이와 불을 순서대로 넣고 bfs를 돌린 후
# 벽을 제외한 가장자리에 지훈이가 있다면 탈출 가능
# 벽은 -1, 지훈이는 1, 불은 -1, 길은 0
# 지훈이는 한 명, 불은 여러 개.
# 지훈이를 가장 먼저 넣고, 불을 그 다음에 넣어.

'''
테케

4 4
####
.JF.
#..#
#..#

4 4
####
#JF.
#..#
##.#

5 5
#J..F
F..##
....#
.#...
#....

5 5
#.F..
F..##
#J..#
.#.F.
#....

'''

from collections import deque

R, C = map(int, input().split())
data = []
JIHUN = (0, 0)
fires = []
for i in range(R):
    input_data = input()
    temp = []
    for j in range(C):
        if input_data[j] == "#":
            temp.append(-1)

        elif input_data[j] == ".":
            temp.append(0)

        elif input_data[j] == "J":
            JIHUN = (i, j)
            temp.append(1)

        elif input_data[j] == "F":
            fires.append((i, j))
            temp.append(-1)

    data.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque(fires)
q.append(JIHUN)

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if data[nx][ny] == 0: # 길인 경우
                if data[x][y] == -1: # 불이 확장
                    data[nx][ny] = -1

                elif data[x][y] >= 1: # 지훈이의 탈출경로
                    data[nx][ny] = data[x][y] + 1

                q.append((nx, ny))

escape = False
esc_time = 1e9
for i in range(R):
    if i == 0 or i == R - 1:
        for j in range(C):
            if data[i][j] >= 1:
                escape = True
                esc_time = min(esc_time, data[i][j])
    else:
        for j in [0, C-1]:
            if data[i][j] >= 1:
                escape = True
                esc_time = min(esc_time, data[i][j])

if escape:
    print(esc_time)
else:
    print("IMPOSSIBLE")