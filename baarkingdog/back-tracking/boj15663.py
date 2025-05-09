N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def back_tracking(sub_arr, used):
    if len(sub_arr) == M:
        print(*sub_arr, sep=" ")
        return

    temp = 0
    for i in range(N):
        if not used[i] and arr[i] != temp:
            used[i] = 1
            sub_arr.append(arr[i])
            temp = arr[i]
            back_tracking(sub_arr, used)
            sub_arr.pop()
            used[i] = 0

back_tracking([], [0] * N)