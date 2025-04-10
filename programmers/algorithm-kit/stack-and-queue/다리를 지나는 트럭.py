from collections import deque

def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) == 1: return bridge_length + 1

    truck_weights = deque(truck_weights)
    q = deque()
    time = 0
    total_weights = 0
    while q or total_weights:
        time += 1

        if q and q[0][1] == time: # 다리를 지날 수 있는 트럭이 있는 경우
            w, _ = q.popleft()
            total_weights -= w

        if truck_weights and total_weights + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            q.append((truck, time + bridge_length))
            total_weights += truck

        return time