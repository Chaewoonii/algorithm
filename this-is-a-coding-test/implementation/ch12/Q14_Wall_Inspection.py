# 335p, 외벽 점검
# 2020 카카오 신입 공채
# https://www.programmers.co.kr/learn/courses/30/lessons/60062

# 완전 탐색
# 원형 데이터 -> 2배로 늘려 원형을 일자로 만들기.

def solution(n, weak, dist):
    walls = [0] * n
    for w in weak:
        walls[w - 1] = 1
    print(walls)

    # 친구들의 외벽 점검: 한 칸씩 옮겨가며 시작, 가장 많은 벽을 보수
    inspection_per_dist = []
    for d in dist:
        d += 1 # 시작 지점을 포함하여 보수할 수 있으므로 +1 해준다.
        w_inspect = 0
        for i in range(len(walls)):
            if i + d <= len(walls):
                # print(walls[i : i + d])
                w_inspect = max(w_inspect, sum(walls[i : i + d]))
            else:
                print(walls[i:] + walls[:d - (len(walls) - i)])
                w_inspect = max(w_inspect, sum(walls[i:] + walls[:d - (len(walls) - i)]))

        inspection_per_dist.append(w_inspect)

    inspection_per_dist.sort(reverse=True)
    friends_cnt = 0
    repaired_walls = 0
    print(inspection_per_dist)
    for w_cnt in inspection_per_dist:
        repaired_walls += w_cnt
        friends_cnt += 1
        if repaired_walls >= len(weak):
            return friends_cnt

    return -1



if __name__ == "__main__":
    # print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

