# 363p, q26-카드 정렬하기, 정렬 / 백준  1715

import heapq

n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sumValue = one + two
    result += sumValue

    heapq.heappush(heap, sumValue)

print(result)
