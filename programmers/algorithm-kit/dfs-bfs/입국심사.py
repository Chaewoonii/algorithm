# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    times.sort()

    left = 1 # 최소시간
    right = times[-1] * n # 최대시간

    while left <= right:
        mid = (left + right) // 2
        entry = count_entry(times, mid)

        if entry >= n:
            answer = mid
            right = mid - 1

        elif entry < n:
            left = mid + 1

    return answer

def count_entry(arr, time):
    return sum([time // a for a in arr])

if __name__ == "__main__":
    print(solution(6, [7, 10]))