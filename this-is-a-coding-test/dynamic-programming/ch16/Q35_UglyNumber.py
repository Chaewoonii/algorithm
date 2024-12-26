# 381p, 못생긴 수

n = int(input())
arr = [1]

temp = 1
while len(arr) <= n:
    arr.append(temp * 2)
    arr.append(temp * 3)
    arr.append(temp * 5)

    temp += 1

arr.sort()
arr = list(set(arr))

print(arr[n-1])
