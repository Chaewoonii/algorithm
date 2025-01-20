# 그리디, 스택(2개)
import copy
def solution(cap, n, deliveries, pickups):
    d_stack = [(deliveries[i], i + 1) for i in range(n) if deliveries[i] > 0]
    p_stack = [(pickups[i], i + 1) for i in range(n) if pickups[i] > 0]

    result = 0
    while True:
        if len(d_stack) <= 0 and len(p_stack) <= 0: break

        d_box, dist = d_stack.pop()





if __name__ == "__main__":
    solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])