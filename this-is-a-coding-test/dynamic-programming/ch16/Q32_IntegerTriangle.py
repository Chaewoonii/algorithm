# 376p, 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

def dp(triangle):
    if len(triangle) > 1:
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

        for i in range(2, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    left = 0
                    right = triangle[i-1][j]

                elif j == len(triangle[i]) - 1:
                    left = triangle[i-1][j-1]
                    right = 0

                else:
                    left = triangle[i-1][j-1]
                    right = triangle[i-1][j]

                triangle[i][j] += max(left, right)

    else:
        return triangle[0][0]

    return max(triangle[len(triangle) - 1])

print(dp(triangle))