#숫자 카드 게임
n, m = map(int, input().split())
result = 0

for i in range(n):
    li = list(map(int, input().split()))
    minNum = min(li)
    result = max(result, minNum)

print(result)