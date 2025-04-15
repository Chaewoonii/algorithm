N = int(input())
stack = [0]
operations = []
i = 1

for _ in range(N):
    num = int(input())

    while stack[len(stack) - 1] < num and i <= N:
        stack.append(i)
        i += 1
        operations.append("+")

    if stack[len(stack) - 1] == num:
        stack.pop()
        operations.append("-")

if len(stack) > 1:
    print("NO")
else:
    print("\n".join(operations))