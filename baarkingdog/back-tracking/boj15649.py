N, M = map(int, input().split())

def func(arr, used):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if not used[i]:
            arr.append(i)
            func(arr, used)
            arr.pop()

func([], [False] * (N+1))