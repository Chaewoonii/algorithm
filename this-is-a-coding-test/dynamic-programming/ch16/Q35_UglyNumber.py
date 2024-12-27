# 381p, 못생긴 수

n = int(input())
arr = {1}

temp = 1
while len(arr) <= n:
    arr.add(temp * 2)
    arr.add(temp * 3)
    arr.add(temp * 5)

    temp += 1

arr = list(arr)
arr.sort()
print(arr[n-1])
