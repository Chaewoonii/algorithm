import sys

input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    op = input().split()
    if op[0] == "push":
        stack.append(op[1])

    elif op[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif op[0] == "size":
        print(len(stack))

    elif op[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    elif op[0] == "top":
        if len(stack) > 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)

