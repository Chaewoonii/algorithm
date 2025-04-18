# 스택의 요소는 ('(', 1)
# ')'이 들어와서 pop을 할 때, 만나는 요소의 값에 곱해준다
# -> 1 * 2
# 그리고, 스택의 탑에 더해준다(값이 1이라면 대체한다)
# (()[[]]) 일 때
# (, 1 | (, 1 !pop!  ), 2 -> 1 * 2
# (, 2
# (, 2 | [, 1 | [, 1 !pop! ] -> 1 * 3
# (, 2 | [, 3 !pop! ] -> 3 * 3
# (, 2 + 9 -> 11
# (, 11 !pop! ) -> 22

PS = input()
stack = []
cnt = 0
for p in PS:
    if p in "([":
        stack.append((p, 1))
        continue
    elif not stack: # 닫는 괄호 인데 스택이 빈 경우
        print(0)
        break

    top_p, top_n = stack.pop()
    if (top_p == "(" and p != ")") or (top_p == "[" and p != "]"): # 괄호 쌍이 맞지 않는 경우
        print(0)
        break

    n = 2 if p == ")" else 3 # 소괄호=2, 대괄호=3
    if stack: # 스택에 값이 있다면
        next_p, next_n = stack.pop()
        if next_n == 1: stack.append((next_p, top_n * n))
        else: stack.append((next_p, next_n + (top_n * n)))

    else: # 괄호가 완전히 닫히면 업데이트
        cnt += top_n * n

else:
    print(cnt)

