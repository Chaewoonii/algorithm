N, M = map(int, input().split())
data = list(map(int, input().split()))
data = list(set(data))
data.sort()

def back_tracking(arr):
    if len(arr) == M:
        print(*arr, sep=" ")
        return

    for i in range(len(data)):
        arr.append(data[i])
        back_tracking(arr)
        arr.pop()

back_tracking([])