from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, N+1):
    sub_combi = list(combinations(arr, i))
    for combi in sub_combi:
        if sum(combi) == S:
            count += 1

print(count)