# 실전문제: 위에서 아래로

n = int(input())
arr = [int(input()) for _ in range(n)]
result = sorted(arr, reverse=True)
print(*result)