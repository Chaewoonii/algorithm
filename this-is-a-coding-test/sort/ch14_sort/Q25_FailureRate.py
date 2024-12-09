# 361p, 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    users = len(stages)
    stages.sort()

    for i in range(1, N + 1):
        cnt = stages.count(i)

        if users == 0:
            answer.append((i, 0))
        else:
            answer.append((i, cnt / users))

        users -= cnt

    answer.sort(key=lambda x: -x[1])
    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))