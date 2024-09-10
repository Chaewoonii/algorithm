# 220p, 개미전사

n = int(input())
arr = list(map(int, input().split()))

dpTable = [0] * 100

dpTable[0] = arr[0]
dpTable[1] = max(arr[0], arr[1])

for i in range(2, n):
    dpTable[i] = max(dpTable[i-1], dpTable[i] + dpTable[i-2])

# print(dpTable)
print(dpTable[n-1])