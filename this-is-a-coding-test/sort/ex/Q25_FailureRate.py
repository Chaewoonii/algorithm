# 361p, q25-실패율, 정렬

def solution(N, stages):
    answer = []
    player = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if player == 0:
            fail = 0
        else:
            fail = count / player

        answer.append((i, fail))
        player -= count

    answer.sort(key=lambda x: -x[1])
    answer = [i[0] for i in answer]

    return answer

#두 번째 예시 틀림
def solution2(N, stages):
    answer = []
    count = [0] * (N + 2)

    for stage in stages:
        count[stage] += 1

    for i in range(1, N+1):
        player = sum(count[i:])
        cnt = count[i]

        if player == 0:
            answer.append((i, 0))
        else:
            answer.append((i, cnt/player))

    answer.sort(key=lambda x: -x[1])
    answer = [i[0] for i in answer]
    return answer

print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution2(4, [4, 4, 4, 4, 4]))