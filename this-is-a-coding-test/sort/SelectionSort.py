#선택 정렬

arr = [7, 5, 9, 0, 3, 1, 2, 6, 4, 8]

for i in range(len(arr)):
    minIdx = i
    for j in range(i + 1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)
