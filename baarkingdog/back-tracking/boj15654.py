N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def back_tracking(sub_arr, used):
    if len(sub_arr) == M:
        print(*sub_arr, sep=" ")
        return

    for i in range(N):
        if used[i]: continue

        sub_arr.append(arr[i])
        used[i] = 1
        back_tracking(sub_arr, used)
        sub_arr.pop()
        used[i] = 0

back_tracking([], [0] * N)