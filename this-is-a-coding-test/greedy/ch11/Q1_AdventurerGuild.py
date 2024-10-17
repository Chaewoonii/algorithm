# 311p, 모험가 길드

n = int(input())
panic = list(map(int, input().split()))

panic.sort()
result = 0
group = 0

for p in panic:
    group += 1
    if p <= group:
        result += 1
        group = 0

print(result)