N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def back_tracking(arr, start):
    if len(arr) == M:
        print(*arr, sep=" ")
        return

    temp = 0
    for i in range(start, N):
        if data[i] != temp:
            arr.append(data[i])
            temp = data[i]
            back_tracking(arr, i+1)
            arr.pop()

back_tracking([], 0)