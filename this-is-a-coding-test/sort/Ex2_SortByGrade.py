# 실전문제2 성적이 낮은 순서로 학생 출력하기

n = int(input())
arr = []

for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

result = sorted(arr, key=(lambda x: x[1]))

for name, grade in arr:
    print(name, end=' ')
