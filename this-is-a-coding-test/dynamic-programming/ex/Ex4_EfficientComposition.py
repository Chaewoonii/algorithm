# 225p, 효율적인 화폐 구성

n, m = map(int, input().split())
currency = [int(input()) for _ in range(n)]
dpTable = [0] * 10001

'''
점화식
해가 없는 경우: -1
m이 15, 화폐가 2, 3일 때
1 -> -1
2 -> 1
3 -> 1
4 -> 3, 1 안됨 2, 2. 2f(2) 
5 -> 4, 1 안됨. f(3) + f(2)
6 -> f(4) + f(2) = f(2) + f(2) + f(2)
7 -> f(5) + f(2)
8 -> f(6) + f(2)
...
n -> f(i-2) + f(2)
'''

'''
점화식 2 4/ 3, 5, 7
1: -1
2: -1
3: 1
4: -1
5: 1
6: f(3) + f(3)
7: 1
8: f(5) + f(3)
9: f(6) + f(3)
...
n -> f(i-3) + f(3)
'''

k = min(currency)
# 점화식: f(i-k) + f(k)
for c in currency:
    dpTable[c] = 1

for i in range(1, m+1):
    if dpTable[i] != 0: continue
    if i < k :
        dpTable[i] = -1
        continue

    if dpTable[i-k] == -1:
        dpTable[i] = -1

    else:
        dpTable[i] = dpTable[i-k] + dpTable[k]

print(dpTable[m])
print(dpTable)