# 375p, 금광

# dp[i][j] = arr[i][j] + max(arr[i-1][j-1], arr[i][j-1], arr[i+1][j-1])
for test_case in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    gold_mine = []
    idx = 0
    for i in range(n):
        gold_mine.append(arr[idx: idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = gold_mine[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = gold_mine[i+1][j-1]

            # 왼쪽에서 오는 경우
            left = gold_mine[i][j-1]

            gold_mine[i][j] = gold_mine[i][j] + max(left_up, left, left_down)

    print(max([i[m-1] for i in gold_mine]))
