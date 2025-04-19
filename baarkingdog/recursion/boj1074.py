N, r, c = map(int, input().split())

# n이 0이면 종료
# n / 2, n/2/2
# 1이 1번
# n/2/2가 2번째 방문
# n/2번이 3번째 방분
# n-n/2/2 가 4번째 방문

def z(n, r, c):
    if n == 0:
        return 0
    else:
        half = 2**n // 2
        if r < half:
            if c < half:
                return z(n-1, r, c) #1번 사각형
            else:
                return half * half + z(n-1, r, c - half) #2번 사각형

        else:
            if c < half:
                return 2 * half * half + z(n-1, r - half, c)

            else:
                return 3 * half * half + z(n-1, r - half, c - half)

print(z(N, r, c))