
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

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(lockAndKey(lock=lock, key=key))