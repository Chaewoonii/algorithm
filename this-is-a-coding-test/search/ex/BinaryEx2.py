# 201p, 떡볶이 떡 만들기 / 백준 나무 자르기, 2805

n, m = map(int, input().split())
riceCakes = list(map(int, input().split()))
# riceCakes.sort()

start = 0
end = max(riceCakes)

result = 0
while start <= end:
    mid = (start + end) // 2
    pieces = 0

    for r in riceCakes:
        if r > mid: pieces += r - mid

    if pieces < m: end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)
