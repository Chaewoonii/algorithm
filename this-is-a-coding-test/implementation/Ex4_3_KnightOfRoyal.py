# 구현 실전문제, 왕실의 나이트

loc = input()
x = ord(loc[0]) - 96
y = int(loc[1])
cnt = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

for s in steps:
    if 0 < x + s[0] < 9 and 0 < y + s[1] < 9:
        cnt += 1

print(cnt)