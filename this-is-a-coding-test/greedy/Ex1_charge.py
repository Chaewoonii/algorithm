#예제 3-1, 거스름돈

num = int(input())
houseCount = 0

coins = [500, 100, 50, 10]

for coin in coins:
    houseCount += num // coin
    num %= coin

print(houseCount)