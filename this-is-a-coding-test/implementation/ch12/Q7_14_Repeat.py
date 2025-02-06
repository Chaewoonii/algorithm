
def print_matrix(matrix):
    print('**')
    for m in matrix:
        print(m)
    print('**')

# 럭키스트레이트
# 123402, 7755
def luckyStraight(n):
    n_arr = list(map(int, n))
    mid = len(n) // 2
    if sum(n_arr[:mid]) == sum(n_arr[mid:]):
        print("LUCKY")
    else:
        print("READY")

# 문자열 재정렬
# K1KA5CB7, AJKDLSI412K4JSJ9D
def stringReordering(string):
    answer = ""
    count = 0
    s_arr = list(string)

    s_arr.sort()

    for s in s_arr:
        if s in list("1234567890"): #str.isalpha() 도 가능
            count += int(s)
        else:
            answer += s

    return answer + str(count)

# 문자열 압축
def stringCompression(s):
    answer = s
    for i in range(1, int(len(s)/2) + 1):
        cnt = 1
        prev = s[:i]
        compression = ""
        for j in range(i, len(s), i):
            sliced = s[j : j + i]

            if j > 0 and prev == sliced:
                cnt += 1
            else:
                compression += str(cnt) + prev if cnt > 1 else prev
                cnt = 1
            prev = sliced

        compression += str(cnt) + prev if cnt > 1 else prev

        if len(compression) < len(answer):
            answer = compression
    return answer

# 자물쇠와 열쇠
# ToDo - 90도 회전, 자물쇠 확장, 열 수 있는지 판단
def turn90(key):
    m = len(key)
    result = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m-1, -1, -1):
            result[i].append(key[j][i])
    return result

def expendLock(lock):
    n = len(lock)
    result = [[0] * (n * 3) for _ in range(n * 3)] # 3배 확장
    for i in range(n):
        for j in range(n):
            result[i + n][j + n] += lock[i][j]
    return result

def isOpen(expended_lock, n):
    for i in range(n):
        for j in range(n):
            if expended_lock[i + n][j + n] != 1:
                return False
    return True

def lockAndKey(lock, key):
    expended_lock = expendLock(lock)
    n = len(lock)
    m = len(key)

    for _ in range(4):
        key = turn90(key) # 열쇠 회전
        # 자물쇠
        for i in range(n * 2):
            for j in range(n * 2):
                #열쇠
                for ki in range(m):
                    for kj in range(m):
                        expended_lock[i + ki][j + kj] += key[ki][kj]

                if isOpen(expended_lock, n):
                    return True

                # 원상복구
                for ki in range(m):
                    for kj in range(m):
                        expended_lock[i + ki][j + kj] -= key[ki][kj]
    return False

# 뱀: 몸은 1, 사과는 2
def changeDirection(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

def snake():
    n = int(input())
    dummy = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(int(input())):
        i, j = map(int, input().split())
        dummy[i][j] = 2 # 사과는 2

    move = []
    l = int(input())
    for _ in range(l):
        t, c = input().split()
        move.append((int(t), c))

    #    우0 하1 좌2 상3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    time = 0
    x, y = 1, 1 # 뱀의 위치
    direction = 0 # 오른쪽부터 시작
    dummy[x][y] = 1
    snake_body = [(x, y)]
    m_idx = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and dummy[nx][ny] != 1:
            if dummy[nx][ny] == 2: # 사과가 있을 경우, 뱀의 몸 길이 늘어남
                dummy[nx][ny] = 1

            elif dummy[nx][ny] == 0: # 사과가 없을 경우, 뱀의 몸 길이 줄어듦
                dummy[nx][ny] = 1
                tail_x, tail_y = snake_body.pop(0)
                dummy[tail_x][tail_y] = 0

            snake_body.append((nx, ny))
            x, y = nx, ny

        else:
            time += 1
            break

        time += 1
        if m_idx < l and time == move[m_idx][0]:
            direction = changeDirection(direction, move[m_idx][1])
            m_idx += 1

    return time

# 기둥과 보 설치
def pillarAndBeams(n, build_frame):
    structure = []
    for order in build_frame:
        x, y, stuff, operation = order
        if operation == 1:
            structure.append([x, y, stuff])
            if not possible(structure):
                structure.remove([x, y, stuff])
        else:
            if [x, y, stuff] in structure:
                structure.remove([x, y, stuff])
                if not possible(structure):
                    structure.append([x, y, stuff])
    return sorted(structure)

# 가능한지 검증
def possible(structure):
    for x, y, stuff in structure:
        # 기둥인 경우: 바닥 위, 보의 한쪽 끝 부분 위, 다른 기둥 위
        if stuff == 0:
            if (y == 0 or
                    [x, y, 1] in structure or
                    [x - 1, y, 1] in structure or
                    [x, y - 1, 0 ] in structure):
                continue
            else:
                return False

        # 보인 경우: 한쪽 끝이 기둥 위, 양쪽 끝이 다른 보와 동시에 연결
        else:
            if ([x, y - 1, 0] in structure or
                    [x + 1, y - 1, 0] in structure or
                    ([x - 1, y, 1] in structure and [x + 1, y, 1] in structure)):
                continue
            else:
                return False
    return True


if __name__ == "__main__":
    print(pillarAndBeams(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    print(pillarAndBeams(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))