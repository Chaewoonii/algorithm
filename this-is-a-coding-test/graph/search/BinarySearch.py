# 188p, 이진탐색
# 탐색하고자 하는 범위의 시작점, 끝점, 중간점 데이터를 활용하여
# 찾으려는 데이터와 중간 위치에 있는 데이터를 반복적으로 비교하여 원하는 데이터를 찾음
# 이미 정렬된 데이터일 경우 빠르게 찾을 수 있음
# O(logN)

# 이진탐색: 재귀함수로 구현
def binarySearch1(arr, target, start, end):
    if start > end: return None

    mid = (start + end) // 2 #중간점
    if arr[mid] == target:
        return mid #target을 찾은 경우 인덱스 반환
    elif arr[mid] > target:
        # target이 중간값보다 작은 경우 왼쪽을 탐색
        return binarySearch1(arr, target, start, mid - 1)
    elif arr[mid] < target:
        # target이 중간값보다 큰 경우 오른쪽을 탐색
        return binarySearch1(arr, target, mid + 1, end)

# 이진탐색: 반복문으로 구현
def binarySearch2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target: return mid
        elif arr[mid] > target: end = mid - 1
        elif arr[mid] < target: start + mid + 1

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binarySearch1(array, target, 0, n - 1)
if result == None: print("원소가 존재하지 않습니다")
else:
    print(result + 1)