# 223p, 바닥 공사

n = int(input())
divNum = 796796

dpTable = [0] * 1000

dpTable[1] = 1
dpTable[2] = 3

# 점화식 f(i) = f(i-1) + 2f(i-2)
for i in range(3, n+1):
    dpTable[i] = dpTable[i-1] + (2 * dpTable[i-2]) % divNum

print(dpTable[n])