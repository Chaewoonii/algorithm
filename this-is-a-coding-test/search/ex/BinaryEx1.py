# 197p 이진탐색 실전문제, 부품칮ㄱ;

import sys

def findTarget(arr, target, start, end):
    if arr[start] <= target <= arr[end]:
        mid = (start + end) // 2

        if arr[mid] == target: return mid
        elif arr[mid] > target: return findTarget(arr, target, start, mid-1)
        elif arr[mid] < target: return findTarget(arr, target, mid+1, end)
    else:
        return None

n = int(input())
items = list(map(int, input().split()))
items.sort()

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    result = findTarget(items, target, 0, n-1)
    if result: print("yes", end=' ')
    else: print("no", end=' ')
