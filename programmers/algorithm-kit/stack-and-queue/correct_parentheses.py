def solution(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0: return False
            stack.pop()

    if len(stack) > 0: return False

    return True