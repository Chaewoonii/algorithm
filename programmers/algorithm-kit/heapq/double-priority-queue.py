import heapq as hq

def solution(operations):
    maxq = []  # 최대힙, -n
    minq = []  # 최소힙, n
    for o in operations:
        order, num = o.split()
        num = int(num)
        if order == "I":
            hq.heappush(maxq, -num)
            hq.heappush(minq, num)

        else:
            if not minq and not maxq: continue
            if num == 1:  # 최댓값 삭재
                deleted = -hq.heappop(maxq)
                minq.remove(deleted)

            elif num == -1:  # 최솟값 삭제
                deleted = -hq.heappop(minq)
                maxq.remove(deleted)

    if minq and maxq:
        return [-hq.heappop(maxq), hq.heappop(minq)]
    return [0, 0]


