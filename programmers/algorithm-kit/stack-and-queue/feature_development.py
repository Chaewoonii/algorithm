def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        flag = True
        while flag:
            if progresses[0] >= 100:
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
                if len(progresses) < 1:
                    if cnt > 0: answer.append(cnt)
                    flag = False
            else:
                if cnt > 0: answer.append(cnt)
                flag = False
    return answer

def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print(f'{-((p - 100) // s)}, {((100-p)//s)}') # 작업을 완료하는데 몇일이 걸리는지 계산: 파이썬의 몫 연산자는 소숫점 버림 연산을 하기 때문에 올림 연산을 위해 음수로 바꾸어 계산 한다
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # 큐가 비어있거나, 배포할 수 없는 경우(작업이 완료되지 않은 경우) 큐에 추가
            Q.append([-((p-100)//s),1])
        else: # 작업이 완료되어 함께 배포할 수 있는 경우
            Q[-1][1]+=1
        # print(Q)
    return [q[1] for q in Q]

print(solution2([93, 30, 55], [1, 30, 5]))
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))