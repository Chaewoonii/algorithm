# 그리디 예제 복습

from itertools import combinations
import heapq

# 1, 모험가 길드
'''
5
2 3 1 2 2
'''
def advanturerGuild():
    n = int(input())
    guild = list(map(int, input().split()))
    guild.sort()

    group_count = 0
    member = 0
    for i in range(n):
        member += 1
        if member <= guild[i]:
            group_count += 1
            member = 0

    print(group_count)

# 2, 곱하기 혹은 더하기
'''
02984
567
'''
def addOrMulti():
    s = list(map(int, list(input())))

    total = s[0]
    for i in range(1, len(s)):
        total = max(total + s[i], total * s[i])

    print(total)

# 3, 문자열 뒤집기
# 001100, 001100110
def stringFilp():
    s = input()
    flip0 = [item for item in list(s.split('0')) if item != '']
    flip1 = [item for item in list(s.split('1')) if item != '']
    # print(flip0, flip1)
    print(min(len(flip0), len(flip1)))


# 4, 만들 수 없는 금액
'''
5
3 2 1 1 9
'''
def cantBeMade():
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()

    target = 1
    for c in coins:
        if target < c: break
        target += c

    print(target)

# 5, 볼링공 고르기
'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''
def bowlingBall():
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    combi = list(combinations(balls, 2))
    for a, b in combi:
        if a == b: combi.remove((a, b))

    print(len(combi))

# 6, 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    used_time = 0
    prev = 0
    length = len(food_times)

    # 사용한 시간 + 이번 음식을 먹는데 덜리는 시간이 k 보다 작을 때 까지 반복
    while used_time + ((q[0][0] - prev) * length)<= k:
        now = heapq.heappop(q)[0] # 현재 먹어야 할 음식, 걸리는 시간
        used_time += (now - prev) * length # 현재 음식을 다 먹는 경우 걸리는 시간: (음식 먹는데 걸리는 시간 - 이전에 보낸 시간(먹은 시간)) * 음식의 개수
        length -= 1 # 한 가지 음식을 다 먹었으므로, 총 음식의 갯수 -1
        prev = now # 음식을 먹는데 소모한 시간 업데이트

    # 남은 음식 중 몇 번째 음식인지 확인 후 출력
    result = sorted(q, key=lambda x: x[1]) # 음식 번호 기준으로 정렬
    target = (k - used_time) % length # 남은 시간 = (k - 사용한 시간) % 남은 음식 갯수
    # 큐에서 남은 시간 번째 요소가 다음으로 먹어야 할 음식.
    return result[target][1]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5