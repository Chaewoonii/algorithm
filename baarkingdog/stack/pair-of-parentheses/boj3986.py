count = 0
for _ in range(int(input())):
    string = input()

    stack = []
    for s in string:
        print(stack)
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    else:
        if not stack: count += 1

print(count)