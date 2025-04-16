from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
q = deque([i for i in range(1, N + 1)])
# 1 2 3 4 5 6 7 8 9 10
# '2' 3 4 5 6 7 8 10 1 -> 오른쪽으로 1회
# '9' 10 1 3 4 5 6 7 8 -> 왼쪽으로 3회
# '5' 6 7 8 10 1 3 4 -> 왼쪽으로 4회 (왼) 9-6+1 = 4 (오) 5
# 왼쪽 이동 vs 오른쪽 이동 값 중 어느게 더 작은지 계산하여 count
# target 인덱스를 찾기
# 왼쪽 이동: idx 값 (왼쪽으로 돌려야 다음 값이 0으로 온다. 0 <- next)
# 오른쪽 이동: len(q) - idx (오른쪽으로 돌려야 이전 값이 1로 온다 prev -> 0)
total = 0
for num in targets:
    idx = q.index(num)
    if idx == 0:
        q.popleft()
        continue

    right = len(q) - idx
    total += min(idx, right)
    q.rotate(-idx if idx <= right else right)
    q.popleft()

print(total)