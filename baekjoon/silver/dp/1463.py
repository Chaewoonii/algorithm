# n = int(input())
# INF = 1e9
# dp = [INF] * (n + 1)
# for i in range(1, n + 1):
#     dp[i] = dp[i - 1] + 1 # 1 을 빼주는 경우
#
#     if i % 2 == 0: # 2로 나누는 것과 1을 더하는 것 중에 연산횟수 더 적은 것을 선택
#         dp[i] = min(dp[i], dp[i//2] + 1)
#
#     if i % 3 == 0: # 2로 나누는 것 또는 1을 더하는 것과 3을 나누는 것 중에 연산 더 적은 것 선택
#         dp[i] = min(dp[i], dp[i//3] + 1)
#
#     # dp[6] = min(dp[5] + 1, dp[3] + 1) -> min(3 + 1, 1 + 1) -> 2
#     # dp[6] = min(2, dp[2] + 1) -> min(2, 1 + 1) -> 2
#
# print(dp)
# print(dp[-1])

n = int(input())
INF = 1e9
dp = [INF] * (n + 1)
dp[1] = 0
for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + 1,
                dp[i//2] + 1 if i % 2 == 0 else INF,
                dp[i//3] + 1 if i % 3 == 0 else INF)

print(dp[-1])