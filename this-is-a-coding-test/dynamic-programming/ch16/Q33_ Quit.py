# 377p, 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())
t = [] # 상담에 걸리는 기간
p = [] # 상담 시 받을 수 있는 금액
dp = [0] * (n + 1)
max_value = 0 # 뒤에서부터 계산, 현재까지의 최대 상담 금액

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 해당 날짜의 상담 금액 + 현재 상담을 마친 일자부터의 최대 이윤
        # 즉 현재 날짜의 이윤 vs 이전에 선택한 날짜의 이윤 중 큰 것을 선택
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i] # 최댓값 갱신
    else:
        dp[i] = max_value # 상담이 기간 안에 끝나지 않는다면 현재까지의 최대 이윤 값으로 업데이트.

print(max_value)

