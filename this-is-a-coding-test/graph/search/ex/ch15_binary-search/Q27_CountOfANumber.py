# 367p, 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

def countOfANumber(arr, x):
    left_idx = bisect_left(arr, x)
    right_idx = bisect_right(arr, x)

    result = right_idx - left_idx
    if result == 0:
        return -1
    else:
        return result

print(countOfANumber(arr, x))
