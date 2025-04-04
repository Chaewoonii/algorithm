def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = [0]
    for i in range(1, N):
        # 현재 값이 stack의 top 보다 클 때까지 stack의 top을 삭제
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx

        stack.append(i)

    # 끝까지 남은 값 처리
    for i in stack:
        answer[i] = N - 1 - i

    return answer