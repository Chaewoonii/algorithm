def solution(priorities, location):
    answer = 0
    Q = [(i, priorities[i]) for i in range(len(priorities))]
    while priorities:
        i, p = Q.pop(0)
        # any 써도 됨: any(): 하나라도 True가 있으면 True를 반환
        if sum(x[1] > p for x in Q) > 0: # 우선순위가 높은 프로세스가 있는 경우
            Q.append((i, p)) # 다시 삽입
        else:
            answer += 1
            if i == location: break
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))