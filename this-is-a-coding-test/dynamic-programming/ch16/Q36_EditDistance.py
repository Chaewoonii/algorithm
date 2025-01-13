# 382p, 편집 거리
# 편집 거리 알고리즘

A = input()
B = input()

n = len(A)
m = len(B)

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = j

        elif j == 0:
            dp[i][j] = i

        else:
            cnt = 0
            if A[i] != B[j]: cnt += 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cnt)

print(dp[n - 1][m - 1])
