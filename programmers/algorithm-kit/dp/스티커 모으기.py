# https://school.programmers.co.kr/learn/courses/18/lessons/1881

def solution(sticker):
    if len(sticker) <= 2: return max(sticker)
    else:
        return max(getMax(sticker[:-1]), getMax(sticker[1:]))

def getMax(sticker):
    N = len(sticker)
    dp = [0] * N
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    for i in range(2, N):
        # 현재 스티커를 선택하지 않는 경우, 선택하는 경우 중 큰 것 선택
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])

    return dp[-1]