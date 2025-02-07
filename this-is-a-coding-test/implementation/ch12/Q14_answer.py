# 친구를 나열하는 모든 경우의 수를 확인, 최소 몇 명 배치하는지 계산
# 조합
# 참고: https://chaemi720.tistory.com/294

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형을 일자형태로
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1# 투입할 친구 수의 최솟값을 찾아야 하므로 친구 수(len(dist)) + 1 로 초기화
    # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 #투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작지점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                if position < weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): return -1 # 투입할 친구가 없다면 종료
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count) # 최솟값 계산
    return answer

if __name__ == "__main__":
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))