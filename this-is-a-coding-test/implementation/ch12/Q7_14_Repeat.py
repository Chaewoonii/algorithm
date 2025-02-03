
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

if __name__ == "__main__":
    pass