# 퀵 정렬: 파이썬의 장점을 살린 짧은 코드

array = [7, 5, 9, 0, 3, 1, 2, 6, 4, 8]

def quickSort(arr):
    if len(arr) <= 1: #원소가 한개면 종료
        return arr

    pivot = arr[0] #피벗(첫 번째 원소)
    tail = arr[1:] #피벗을 제외한 리스트

    leftSide = [x for x in tail if x <= pivot] #왼쪽 분할
    rightSide = [x for x in tail if x > pivot] # 오른쪽 분할

    #분할 이후 왼쪽, 오른쪽 정렬 수행, 전체 리스트 반환
    return quickSort(leftSide) + [pivot] + quickSort(rightSide)

print(quickSort(array))
