N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def back_tracking(sub_arr, start):
    if len(sub_arr) == M:
        print(*sub_arr, sep=" ")
        return

    for i in range(start, N):
        if arr[i] in sub_arr: continue
        sub_arr.append(arr[i])
        back_tracking(sub_arr, i + 1)
        sub_arr.pop()

back_tracking([], 0)