n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(i, now):
    global mx, mn

    if i == n - 1:
        mx = max(now, mx)
        mn = min(now, mn)
        return

    if ops[0] != 0:  # 덧셈
        ops[0] -= 1
        dfs(i + 1, now + nums[i + 1])
        ops[0] += 1

    if ops[1] != 0:  # 뺄셈
        ops[1] -= 1
        dfs(i + 1, now - nums[i + 1])
        ops[1] += 1

    if ops[2] != 0:  # 곱셈
        ops[2] -= 1
        dfs(i + 1, now * nums[i + 1])
        ops[2] += 1

    if ops[3] != 0:
        ops[3] -= 1
        dfs(i + 1, int(now / nums[i + 1]))
        ops[3] += 1

dfs(0, nums[0])
print(mx)
print(mn)
