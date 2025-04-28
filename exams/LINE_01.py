'''
1번 문제: 조합
점수, 테케 *n개 형식
응시자가 가능한 점수

[[6, 2], [4, 2]] -> 11
[[10, 1], [1, 1], [3, 2]] -> 0, 1, 2, 3, 4, 10, 11, 12, 13, 14
'''
from itertools import product
def solution(problems):
    scores = []
    results = set()
    for p, t in problems:
        if t == 1:
            scores.append([0, p])
        else:
            scores.append([i for i in range(p+1)])

    combi = list(product(*scores))
    for c in combi:
        results.add(sum(c))
    print(results)
    return len(results)

print(solution([[6, 2], [4, 2]]))
print(solution([[10, 1], [1, 1], [3, 2]]))