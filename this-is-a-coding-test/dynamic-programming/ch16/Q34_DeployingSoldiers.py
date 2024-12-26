# 380p, 병사 배치하기
# https://www.acmicpc.net/problem/18353
# LIS: Longest Increasing Subsequence
# 가장 긴 증가하는 부분 수열

# 12, 15 11 4 8 10 5 3 2 4 3 4 1
# 7, 15 11 4 9 5 2 4

n = int(input())
arr = list(map(int, input().split()))
arr.reverse() # 오름차순으로 만들어야 LIS로 풀이 가능.

dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외 시켜야 하는 병사의 최소 수: 병사의 총 수 - LIS 길이
print(n - max(dp))