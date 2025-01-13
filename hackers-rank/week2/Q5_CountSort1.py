# hackers rank week2, Counting Sort 1
# 계수정렬

def countingSort(arr):
    result = [0] * 100
    for num in arr:
        result[num] += 1
    return result