# 슬라이딩 윈도우

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split())) # 로테이션은 필요 없다.
q = deque() # 윈도우의 최솟값 인덱스를 저장
result = []
for i in range(N):
    # 현재 윈도우에 들어올 값보다 큰 값들은 제거
    # 즉, 큐의 마지막 값이 현재 값 보다 크다면 큐에서 제거
    while q and arr[q[-1]] > arr[i]:
        q.pop()

    q.append(i) # 현재 값의 인덱스를 넣는다.

    # 윈도우 범위에서 벗어난 것 제거
    if q[0] <= i - L:
        q.popleft()

    result.append(str(arr[q[0]])) # 결과 저장

print(" ".join(result))