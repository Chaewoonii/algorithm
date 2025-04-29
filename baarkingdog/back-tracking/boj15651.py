N, M = map(int, input().split())

def back_tracking(arr):
    if len(arr) == M:
        print(*arr, sep=" ")
        return

    for i in range(1, N+1):
        arr.append(i)
        back_tracking(arr)
        arr.pop()

back_tracking([])