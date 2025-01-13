# 368p, 고정점 찾기


# arr[idx](1) < idx(2) 인 경우 오른쪽 탐색
# arr[idx](7) > idx(4) 인 경우 왼쪽 탐색
#       0   1   2  3  4
#       >   >   >  =  <
# arr = [-15, -5, 1, 3, 7]

n = int(input())
arr = list(map(int, input().split()))

def findFixedPoint(arr, start, end):
    if start > end: return -1

    mid = (start + end) // 2 # 중간값

    if arr[mid] == mid: # target
        return mid
    elif arr[mid] > mid: # 왼쪽 탐색
        return findFixedPoint(arr, start, mid - 1)
    elif arr[mid] < mid: # 오른쪽 탐색
        return findFixedPoint(arr, mid + 1, end)



print(findFixedPoint(arr, 0, n - 1))