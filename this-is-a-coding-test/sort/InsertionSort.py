#삽입 정렬

arr = [7, 5, 9, 0, 3, 1, 2, 6, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)
