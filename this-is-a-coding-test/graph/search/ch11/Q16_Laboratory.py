# 341p, 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]
dRow = [0, 1, 0, -1]
dCol = [1, 0, -1, 0]

# 바이러스 좌표 저장
def findVirusAndEmptySpace(laboratory):
    virus = []
    empty_space = []
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 2:
                virus.append((i, j))
            elif laboratory[i][j] == 0:
                empty_space.append((i, j))
    return virus, empty_space

# 바이러스 전파
def spreadVirusBFS(laboratory, start):
    queue = deque([start])
    laboratory[start[0]][start[1]] = 2

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if 0 <= nRow < n and 0 <= nCol < m:
                if laboratory[nRow][nCol] == 0:
                    queue.append((nRow, nCol))
                    laboratory[nRow][nCol] = 2
    return laboratory

# 안전영역 크기
def countSafeSpace(laboratory):
    count = 0
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 0:
                count += 1
    return count


# 3가지 조합으로 완전 탐색
    # 1. 벽 세우기
    # 2. 바이러스 퍼트리기(BFS)
    # 3. 안전 영역 크기 구하기(최댓값으로 update)
def solution(laboratory):
    virus, empty_space = findVirusAndEmptySpace(laboratory) # 바이러스 위치와 빈 공간 구하기
    combi_walls = list(combinations(empty_space, 3)) # 조합 구하기
    max_safe_space = 0

    for combi in combi_walls:
        lab = copy.deepcopy(laboratory)
        # 벽 세우기
        for wall in combi:
            lab[wall[0]][wall[1]] = 1
        # 바이러스 퍼트리기
        for item in virus:
            lab = spreadVirusBFS(lab, item)
        # 안전 영역 크기 구하기
        max_safe_space = max(countSafeSpace(lab), max_safe_space)

    return max_safe_space

print(solution(laboratory))


