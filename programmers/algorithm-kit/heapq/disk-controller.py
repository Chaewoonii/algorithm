import heapq as hq


def solution(jobs):
    jobs.sort() # 요청 시각 순 정렬
    total = 0 # 반환 시간 총합
    waiting = [] # 대기 큐
    idx = 0 # 작업 번호
    cnt = len(jobs) # 남은 작업의 개수
    time = 0 # 현재 시간

    while cnt > 0: #모든 작업을 완료 할 때까지
        # 현재 시간 까지의 요청 작업을 대기 큐에 삽입
        while idx < len(jobs) and jobs[idx][0] <= time:
            req_time, duration = jobs[idx]
            hq.heappush(waiting, (duration, req_time))
            idx += 1

        # 대기 큐에 작업이 있다면
        if waiting:
            duration, req_time = hq.heappop(waiting) #작업 꺼내기
            time += duration # 작업 끝내기, 현재 시간 갱신
            total += time - req_time # 반환 시간 계산 (총합)
            cnt -= 1 # 남은 작업의 개수 갱신

        # 대기 큐에 작업이 없다면
        else:
            time = jobs[idx][0] # 다음 작업 요청 시각으로 넘어가기

    return total // len(jobs)

print(solution([[0, 3], [1, 9], [3, 5]]))
