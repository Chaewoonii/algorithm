N, M = map(int, input().split())

def back_tracking(arr, start):
    if len(arr) == M:
        print(*arr, sep=" ")
        return

    for i in range(start, N+1):
        if i in arr: continue

        arr.append(i)
        back_tracking(arr, i+1) # i 이후의 수만 쓸 수 있다.
        arr.pop()

back_tracking([], 1)

N, M = map(int, input().split())

