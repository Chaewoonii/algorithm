# 351p, 감시 피하기
# https://www.acmicpc.net/problem/18428

from itertools import combinations
import copy

n = int(input())
hall = []
teachers = []
spaces = []

for i in range(n):
    data = list(input().split())
    hall.append(data)

    for j in range(n):
        if data[j] == 'T': teachers.append((i, j))
        elif data[j] == 'X': spaces.append((i, j))

def monitoring(row, col, hall):
    # 상하: 0~row, row~n / 좌우: 0~col, col~n
    # 상
    for i in range(row, -1, -1):
        if hall[i][col] == 'S': return False
        elif hall[i][col] == 'O': break
    # 하
    for i in range(row, n):
        if hall[i][col] == 'S': return False
        elif hall[i][col] == 'O': break
    # 좌
    for i in range(col, -1, -1):
        if hall[row][i] == 'S': return False
        elif hall[row][i] == 'O': break
    # 우
    for i in range(col, n):
        if hall[row][i] == 'S': return False
        elif hall[row][i] == 'O': break

    return True

def process():
    combies = combinations(spaces, 3)

    for combi in combies:
        hall_copy = copy.deepcopy(hall)
        flag = len(teachers)
        for cx, cy in combi:
            hall_copy[cx][cy] = 'O'

        for tx, ty in teachers:
            if monitoring(tx, ty, hall_copy) is True: flag -= 1

        if flag == 0: return True

    return False

if process() is True: print("YES")
else: print("NO")