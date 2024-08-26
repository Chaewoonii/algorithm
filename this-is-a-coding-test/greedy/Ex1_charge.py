#예제 3-1, 거스름돈

num = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += num // coin
    num %= coin

print(count)