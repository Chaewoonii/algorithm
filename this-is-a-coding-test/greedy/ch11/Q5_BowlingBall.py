# 315p, 볼링공 고르기

n, m = map(int, input().split())
balls = list(map(int, input().split()))

count = 0
for i in range(n):
    for ball in balls[i:]:
        if balls[i] != ball:
            count += 1

print(count)
