# 상하좌우
upDown, rightLeft = 1, 1
n = int(input())
moves = input().split()

for m in moves:
    if m == "U":
        if upDown > 1: upDown -= 1

    elif m == "D":
        if upDown < 5: upDown += 1

    elif m == "R":
        if rightLeft < 5: rightLeft += 1

    elif m == "L":
        if rightLeft > 1: rightLeft += 1

print(upDown, rightLeft)