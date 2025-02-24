# pokemon buddy
for _ in range(int(input())):
    # group = [0, 1, 3, 5]
    g, c, e = map(int, input().split())
    print((e-c) * (2*g - 1) if c < e else 0)
    # print((e-c) * group[g] if c < e else 0)
    # print(max(e-c, 0) * (2*g - 1))
