# 346p, 괄호 변환
# programmers.co.kr/learn/courses/30/lessons/60058

def getBalancedIdx(string):
    cnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i

def checkUprightParentheses(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    idx = getBalancedIdx(p)
    u = p[:idx + 1]
    v = p[idx + 1:]
    if checkUprightParentheses(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer

print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
