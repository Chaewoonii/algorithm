# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = [0] + rocks + [distance]
    left = 0
    right = distance

    # 최소가 0, 최대가 도착점으로 설정, 거리의 최솟값을 mid로 설정하여 이분탐색
    while left <= right:
        mid = (left + right) // 2 # 바위 간 거리로 가정
        deleted = deleteRocks(rocks, mid)

        if deleted > n:  # 삭제되는 바위의 개수가 n보다 크면 mid를 줄인다
            right = mid - 1

        elif deleted <= n:  # 삭제되는 바위의 개수가 n이하라면 mid를 키운다
            answer = mid
            left = mid + 1

    return answer

# 최소 거리를 dist로 설정했을 때 삭제되는 바위의 개수
def deleteRocks(rocks, dist):
    prev = 0  # 출발점
    deleted = 0  # 제거한 바위 개수
    for i in range(1, len(rocks)):
        if rocks[i] - prev < dist:  # 현재와 이전 바위의 거리가 dist보다 작으면 바위 제거
            deleted += 1
        else:
            prev = rocks[i]  # dist보다 크면(거리가 충분하면) 바위 유지, prev 갱신
    return deleted

x = 2
y = 4
