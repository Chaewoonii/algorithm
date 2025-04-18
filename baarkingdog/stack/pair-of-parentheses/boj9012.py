for _ in range(int(input())):
    PS = input()

    stack = []
    for p in PS:
        if p == "(":
            stack.append(p)
        elif stack and stack[-1] == "(" and p == ")":
            stack.pop()
        else:
            print("NO")
            break
    else:
        if stack: print("NO")
        else: print("YES")