import sys
input = sys.stdin.readline
# 6 9 5 7 10 4
# 0 0 2 2 0 5
N = int(input())
tops = list(map(lambda x: (x[0], int(x[1])), enumerate(input().split())))
result = ["0"] * N
# 뒤에서 부터 순서대로 스택에 넣는다.
# 스택의 탑보다 작다면 스택에 넣는다
# 스택의 탑보다 크다면 탑이 숫자보다 작아질때까지 스택의 탑을 삭제한다.
# 남아있는 스택의 숫자들은 0으로 표기한다.
# 4 7 -> 7
# 7 5 -> 9
# 9 6
stack = []
while tops:
    i, t = tops.pop()
    if not stack:
        stack.append((i, t))
    else:
        while stack and stack[len(stack) - 1][1] < t:
            i2, t2 = stack.pop()
            result[i2] = f"{i + 1}"
        stack.append((i, t))

print(" ".join(result))
