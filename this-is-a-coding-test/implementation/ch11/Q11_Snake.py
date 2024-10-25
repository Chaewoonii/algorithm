# 327p, 뱀
# 삼성전자 sw 역량테스트
# acmicpc.net/problem/3190
import copy
n = int(input()) # 보드 크기
dummy_map = [[0] * (n + 1) for _ in range(n + 1)] # 지도
k = int(input()) # 사과 개수
info = [] # 이동 정보

# 사과 정보 저장
for _ in range(k):
    a, b = map(int, input().split())
    dummy_map[a][b] = 1

l = int(input()) # 뱀 방향 변환 횟수
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

#뱀의 이동은 큐를 활용!
def solution():
    x, y = 1, 1 # 시작점
    dummy_map[x][y] = 2 # 뱀의 머리
    direction = 0
    time = 0

    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보

    while True:
        time += 1
        info_idx = 0
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 뱀이 맵 안에 있고, 뱀의 몸통과 닿지 않은 경우
        if 1 <= nx <= n and 1 <= ny <= n and dummy_map[nx][ny] != 2:
            # 사과가 없는 경우
            if dummy_map[nx][ny] == 0:
                # 뱀 이동
                dummy_map[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop()
                dummy_map[px][py] = 0

            # 사과를 만난 경우
            elif dummy_map[nx][ny] == 1:
                q.append((nx, ny))
                dummy_map[nx][ny] = 2
        else:
            break

        x, y = nx, ny # 위치 이동
        if time == info[info_idx][0]:
            direction = turn(direction, info[info_idx][1])
            info_idx += 1

    return time