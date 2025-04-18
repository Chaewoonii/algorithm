
while True:
    string = input()
    if string == ".": break

    stack = []
    for s in string:
        if s in "()[]":
            if s in "([":
                stack.append(s)

            elif stack and stack[-1] == '(' and s == ')':
                stack.pop()

            elif stack and stack[-1] == '[' and s == ']':
                stack.pop()
            else:
                print("no")
                break
        else:
            continue

    else:
        if stack: print("no")
        else: print("yes")
