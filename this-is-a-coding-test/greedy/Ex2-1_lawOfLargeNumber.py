#2, 예제1-큰 수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort()
maxNum = arr[len(arr) - 1]
sndNum = arr[len(arr) - 2]

while m:
    for i in range(k):
        answer += maxNum
        m -= 1
    answer += sndNum
    m -= 1

print(answer)

