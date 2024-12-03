# 363p, 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
cards = []

for i in range(n):
    heapq.heappush(cards, int(input()))

sumValue = 0
result = 0
while len(cards) > 1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)

    sumValue = n1 + n2
    result += sumValue

    heapq.heappush(cards, sumValue)

print(result)
# 10 20 30 50 일 때
# (10+20) + (30+40) + (70+50)