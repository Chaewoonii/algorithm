#      북 동 남 서
# 방향은 1, 2, 3, 4
# 90도 회전: 각 방향에 +1 % 4
#
import copy
from itertools import product


def direction_of_cctv(number):
    if number == 1:
        return [(0), (1), (2), (3)]
    elif number == 2:
        return [(0, 2), (1, 3)]
    elif number == 3:
        return [(0, 1), (1, 2), (2, 3), (3, 0)]
    elif number == 4:
        return [(0, 1, 3), (0, 1, 2), (1, 2, 3), (2, 3, 0)]
    elif number == 5:
        return [(0, 1, 2, 3)]

def watch(x, y, direction, map_data):
    #    북  동  남  서
    #     0   1  2  3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for d in direction:
        i = 1
        while True:
            nx = x + (dx[d] * i)
            ny = y + (dy[d] * i)
            if 0 <= nx < N and 0 <= ny < M and map_data[nx][ny] != 6:
                map_data[nx][ny] = "#"
            else:
                break
            i += 1

    return map_data

def count_blind_space(map_data):
    return sum(1 for row in map_data for cell in row if cell == 0)

N, M = map(int, input().split())
data = []
cctv_locations = []
cctv_directions = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:
          cctv_locations.append((i, j, row[j])) # x, y, cctv 번호
          cctv_directions.append(direction_of_cctv(row[j]))
    data.append(row)

# cctv 방향 조합
combies = list(product(*cctv_directions))
blank_space = 1e9
for combi in combies:
    temp_map = copy.deepcopy(data)
    for i in range(len(combi)):
        x, y, n = cctv_locations[i]
        temp_map = watch(x, y, combi[i] if n > 1 else [combi[i]], temp_map)

    blank_space = min(blank_space, count_blind_space(temp_map))

print(blank_space)