# 골뱅이 찍기
n = int(input())
cell = 5 * n
for i in range(cell):
    if i >= cell - n or 2 * n - 1 < i < 2 * n + n:
        print("@" * cell)
    else:
        print(("@" * n) + (" " * (cell - 2 * n)) +("@" * n))
