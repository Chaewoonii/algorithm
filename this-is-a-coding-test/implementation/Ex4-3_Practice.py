# 왕실의 기사 연습

location = input()
# xArr = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# x = xArr.index(location[0])
x = ord(location[0]) - 96
y = int(location[1])
move = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# print(location, x, y)

cnt = 0
for m in move:
    if 0 < m[0] + x < 9 and 0 < m[1] + y < 9:
        cnt += 1

print(cnt)