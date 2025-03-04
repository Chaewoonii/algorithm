import heapq as hq


def solution(jobs):
    t = 0
    total = 0
    q = []
    for j in jobs:
        hq.heappush(q, (j[1], j[0], 0))

    while q:
        print(q)
        wt, wn, w = hq.heappop(q)
        if w == wt:
            total += t - wn
        else:
            hq.heappush(q, (wt, wn, w + 1))
        t += 1

    return total // len(jobs)

print(solution([[0, 3], [1, 9], [3, 5]]))
