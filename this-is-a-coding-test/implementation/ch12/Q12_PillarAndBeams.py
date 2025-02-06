# 329p, 기둥과 보 설치
# 2020 카카오 신입 공채
# https://www.programmers.co.kr/learn/courses/30/lessons/60061

# 0 기둥, 1 보 // 표시: 기둥 2, 보 1
# 0 삭제, 1 설치
def build(n, build_frame):
    structures = []
    for order in build_frame:
        x, y, stuff, operation = order
        # 설치
        if operation == 1:
            structures.append([x, y, stuff])
            if not possible_to_order(structures):
                structures.remove([x, y, stuff])

        # 삭제
        else:
            if [x, y, stuff] in structures:
                structures.remove([x, y, stuff])
                if not possible_to_order(structures):
                    structures.append([x, y, stuff])
    return sorted(structures)

# 가능한 명령인지 확인: 명령 실행 후 구조물이 '존재 가능한지' 전체 탐색
def possible_to_order(structures):
    for x, y, stuff in structures:
        # 기둥인 경우: 보의 한쪽 끝 부분 위 혹은 기둥 위, 바닥 위
        if stuff == 0:
            if (y == 0 or
                    [x-1, y, 1] in structures or
                    [x, y, 1] in structures or
                    [x, y - 1, 0] in structures):
                continue
            else: return False

        # 보인 경우: 한 쪽 끝이 기둥이거나 양 쪽 끝이 보, 바닥은 안됨
        elif stuff == 1:
            if ([x, y - 1, 0] in structures or
                    [x + 1, y - 1, 0] in structures or
                    ([x + 1, y, 1]in structures and [x - 1, y, 1] in structures)):
                continue
            else: return False
    return True


if __name__ == "__main__":
    n = 5
    build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(build(n, build_frame1))
    print(build(n, build_frame2))