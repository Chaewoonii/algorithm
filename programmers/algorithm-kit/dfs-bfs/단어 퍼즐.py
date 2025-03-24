# https://school.programmers.co.kr/learn/courses/18/lessons/1882
from collections import deque

# BFS 풀이. dfs로 풀면 시간초과 걸림
def solution(strs, t):
    strs = set(strs) # 중복 제거, 검색시간 O(1)
    q = deque([(0, 0)]) # idx, cnt
    visited = {0} # 방문 여부, set으로 관리
    max_len = max(map(len, strs))

    while q:
        i, cnt = q.popleft()

        # i 다음(i+1) 부터 가장 긴 문자열의 길이(+max_len)까지 탐색한다.
        # i + 1 + max_len 이 len(t)보다 클 수 있으므로 최소조건을 걸어준다(min)
        # reversed: 가장 긴 문자열부터 탐색
        for j in reversed(range(i + 1, min(i + 1 + max_len, len(t) +1))):
            if t[i:j] in strs and j not in visited: # t[i:j]가 strs에 있고 해당 위치를 방문하지 않은 경우
                if j == len(t): return cnt + 1 # 끝에 도달
                q.append((j, cnt + 1)) # 다음으로 이동
                visited.add(j) # 방문

    return -1 # 문자열을 만들 수 없는 경우

# dfs 풀이(완탐) - 시간초과
INF = 1e9
def solution2(strs, t):
    strs = set(strs)
    max_len = max(map(len, strs))
    visited = set([0])
    min_cnt = INF

    def dfs(i, cnt):
        nonlocal min_cnt
        if i == len(t):
            min_cnt = min(min_cnt, cnt)
            return cnt

        for j in range(i + 1, min(i + max_len + 1, len(t) + 1)):
            if t[i:j] in strs and j not in visited:
                visited.add(j)
                result = dfs(j, cnt + 1)

                if result != -1:
                    min_cnt = min(min_cnt, result)

                visited.remove(j)

        return -1

    dfs(0, 0)
    return min_cnt if min_cnt != INF else -1

