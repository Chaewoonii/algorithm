N, M = map(int, input().split())

def back_tracking(arr, start):
    if len(arr) == M:
        print(*arr, sep=" ")
        return

    for i in range(start, N+1):
        arr.append(i)
        back_tracking(arr, i)
        arr.pop()

back_tracking([], 1)