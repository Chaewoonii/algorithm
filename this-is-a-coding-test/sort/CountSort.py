# 계수 정렬
# 가장 큰 데이터(수)보다 1 큰 배열을 선언, 수가 등장한 기록 count

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(arr) + 1) #모든 범위를 포함하는 리스트 선언

for num in arr:
    count[num] += 1 # 수 등장 기록, 해당 수의 인덱스에 카운트

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') #인덱스에 기록된 정보, 즉 수가 등장한 횟수만큼 출력



