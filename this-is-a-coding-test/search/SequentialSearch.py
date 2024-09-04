# 186p, 순차탐색
# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 하나씩 차례대로 확인

# arr을 순차적으로 확인하며 target을 찾고, 인덱스(i)를 반환
def sequentialSearch(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i


inputData = input().split()
n = int(inputData[0])
target = inputData[1]

array = input().split()

idx = sequentialSearch(n, target, array)
print(idx + 1)