N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def back_tracking(sub_arr):
    if len(sub_arr) == M:
        print(*sub_arr, sep=" ")
        return

    for i in range(N):
        sub_arr.append(arr[i])
        back_tracking(sub_arr)
        sub_arr.pop()


back_tracking([])