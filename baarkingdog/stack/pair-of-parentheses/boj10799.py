# 스택에 ( 를 쌓는다
# 이전 값을 저장한다. 이전 값이 (이고, 현재 값이 )이면 ()이면 레이저이다
# 레이저를 만났을 때는 스택의 길이 만큼 count에 추가한다
# )가 레이저가 아닌 막대의 끝이라면 1 count에 1을 추가한다.

count = 0
data = input()
stack = []
prev = ""
for d in data:
    if d == "(":
        stack.append(d)
    else:
        stack.pop()
        if prev == "(": # 레이저인 경우
            count += len(stack)
        else:
            count += 1
    prev = d

print(count)