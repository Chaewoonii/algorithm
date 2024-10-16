# 314p, 만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
for c in coins:
    print(target)
    if target < c:
        break
    target += c

print(target)

'''
target 값에 coin을 더해 '만들 수 있는 수' 를 업데이트.
target에 coin을 더한 값: target-1 까지의 모든 금액을 만들 수 있음
1부터 축적되기 때문에, target은 더해진 coin으로 만들 수 있는 값의 최대를 의미
따라서 ~target까지의 모든 수를 coin을 조합하여 만들 수 있는 것임.

예시 1
1 2 3 5
t   c
1 + 1 = 2 [1] -> 1까지 만들 수 있음
2 + 2 = 4 [1, 2] -> 3까지 만들 수 있음
4 + 3 = 7 [1, 2, 3] -> 6까지 만들 수 있음
7 + 5 = 12 [1, 2, 3, 5] -> 11까지 만들 수 있음
12 (없음)
답은 12

예시 2
3 2 1 1 9 -(sort)-> 1 1 2 3 9
t   c
1 + 1 = 2 [1] -> 1 만들 수 있음
2 + 1 = 3 [1, 1] -> 2 까지 만들 수 있음
3 + 2 = 5 [1, 1, 2] -> 4까지 만들 수 있음
5 + 3 = 8 [1, 1, 2, 3] -> 7까지 만들 수 있음
8 < 9: break -> 다음 동전이 t값(8)보다 크므로 8을 만들 수 없음
답은 8
'''