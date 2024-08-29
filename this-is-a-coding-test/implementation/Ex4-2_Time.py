# 예제 4-2, 시각
n = int(input())
houseCount = 0

# 00시 00분 00초부터 n시 59분 59초까지 세야 하므로 range(n+1)로 설정.
# 예를 들면, n이 5일 경우 range(5)으로 설정하면 반복문이 5번 수행되며, 0, 1, 2, 3, 4까지 수행된다.
# 즉, 00시 00분 00초부터 4시 59분 59초까지만 숫자를 세게 된다.
# 따라서, 5시 59분 59초까지 카운트하기 위해서는 range(6), 즉, range(n+1)로 설정해야한다
# range(n)일 경우: n = 5일 때 0, 1, 2, 3, 4
# range(n+1)일 경우: n = 5일 때 0, 1, 2, 3, 4, 5

for t in range(n + 1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(n) + str(min) + str(sec):
                houseCount += 1
    n -= 1

print(houseCount)