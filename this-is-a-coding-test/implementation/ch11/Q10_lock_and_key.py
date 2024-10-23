# 325p, 자물쇠와 열쇠
# 2020 카카오 신입 공채
# programmers.co.kr/learn/courses/30/lessons/60059

'''
000
100
011

+90
010
100
100

+180
110
001
000

+270
001
001
010

'''

import copy

def turn90(key):
    result = [[] for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key[i])-1, -1, -1):
            result[i].append(key[j][i])

    return result

def check_lock(expended_lock, lock_length):
    for i in range(lock_length):
        for j in range(lock_length):
            if expended_lock[i + lock_length][j + lock_length] != 1:
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    expended_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            expended_lock[i + n][j + n] += lock[i][j]

    for _ in range(4):
        key = turn90(key)
        # 자물쇠 전체 돌기
        for i in range(n * 2):
            for j in range(n * 2):
                # 열쇠 돌기
                for ki in range(m):
                    for kj in range(m):
                        expended_lock[i + ki][j + kj] += key[ki][kj]

                if check_lock(expended_lock, n):
                    return True

                # 원상복구
                for ki in range(m):
                    for kj in range(m):
                        expended_lock[i + ki][j + kj] -= key[ki][kj]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))