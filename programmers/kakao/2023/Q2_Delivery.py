# 그리디, 스택(2개)

def solution(cap, n, deliveries, pickups):
    d_stack = [(deliveries[i], i + 1) for i in range(n) if deliveries[i] > 0]
    p_stack = [(pickups[i], i + 1) for i in range(n) if pickups[i] > 0]

    result = 0
    while len(d_stack) + len(p_stack) > 0:
        # 가장 먼 집 계산
        max_dist = 0
        if d_stack: max_dist = max(max_dist, d_stack[-1][1])
        if p_stack: max_dist = max(max_dist, p_stack[-1][1])

        # 왕복 거리 추가
        result += max_dist * 2

        # 배달
        d_cap = cap
        while d_stack and d_cap > 0:
            d_box, dist = d_stack.pop()
            if d_cap < d_box:
                d_stack.append((d_box - d_cap, dist))
                break
            else:
                d_cap -= d_box

        # 수거
        p_cap = cap
        while p_stack and p_cap > 0:
            p_box, dist = p_stack.pop()
            if p_cap < p_box:
                p_stack.append((p_box - p_cap, dist))
                break
            else:
                p_cap -= p_box

    return result


if __name__ == "__main__":
    result = solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
    print(result)