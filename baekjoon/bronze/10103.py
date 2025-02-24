# 주사위 게임
player1, player2 = 100, 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b: continue
    elif a > b: player2 -= a
    else: player1 -= b

print(player1)
print(player2)