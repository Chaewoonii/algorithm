# 312p, 곱하기 혹은 더하기

n = list(map(int, list(input())))
result = n[0]

for i in range(1, len(n)):
    add = result + n[i]
    multi = result * n[i]

    result = max(add, multi)

print(result)