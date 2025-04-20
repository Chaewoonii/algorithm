'''
쿠폰을 수정하자
숫자를 수정하려는 시도가 있을 수 있음
같은 위치에 같은 알파벳이 있따면 수정해야할 대상
총 수정 횟수를 구하기

예: ["AAA01", "AAA02", "AAA03", "BBB04", "BBB02"] -> 3회
["01A", "A01", "A12", "A22"] -> 2회
'''

def solution(code):
    code_dict = {}
    count = 0
    for c in code:
        key = [] # 야매 정규식을 키로 만든다.
        for s in c:
            if s.isdigit():
                key.append("\d")
            else:
                key.append(s)
        key = "".join(key)
        if key in code_dict.keys(): # 같은 정규식이 키에 있다면
            count += 1 # 수정 횟수에 더해주고
            code_dict[key] += 1 # 몇개인지 세준다
        else:
            code_dict[key] = 1 # 키가 없다면 만들어준다
    print(code_dict)
    return count

print(solution(["AAA01", "AAA02", "AAA03", "BBB04", "BBB02"]))
print(solution(["01A", "A01", "A12", "A22"]))
