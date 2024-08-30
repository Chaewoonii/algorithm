# 퀵 정렬
arr = [7, 5, 9, 0, 3, 1, 2, 6, 4, 8]

def quickSort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start
    left = start + 1 #피벗보다 큰 데이터를 탐색하기 위한 인덱스값
    right = end #피벗보다 작은 데이터를 탐색하기 위한 인덱스값

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복(선형 탐색)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복(선형 탐색)
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 찾은 데이터가 엇갈렸다면 작은 데이터와 피벗의 위치를 교체 -> 바뀐 피벗 위치를 기준으로 데이터 분할
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터의 위치를 교체
            array[left], array[right] = array[right], array[left]

    # while left <= right를 빠져나온 후(즉, 찾는 데이터가 엇갈리고, 피벗의 위치가 교체된 후)
    # 바뀐 피벗 위치를 기중으로 데이터 분할, 오른쪽과 왼쪽에서 각각 퀵정렬 재귀적으로 수행
    quickSort(array, start, right - 1) # 다시 시작 지점(왼쪽)부터 탐색
    quickSort(array, right+1, end) #다시 끝 지점(오른쪽)부터 탐색

quickSort(arr, 0, len(arr) - 1)
print(arr)