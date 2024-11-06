# hackers rank week1, Camel Case 4
# 조건에 따라 카멜케이스 작성 또는 분리하기

import sys

def solution(data):
    answer = data[2].strip()
    if data[0] == 'S':
        if data[1] == 'M' and '()' in answer:
            answer = answer.replace('()', '')

        answer = list(answer)
        for i in range(len(answer)):
            if answer[i].isupper():
                if i != 0:
                    answer[i] = ' ' + answer[i].lower()
                else:
                    answer[i] = answer[i].lower()

        answer = ''.join(answer)

    elif data[0] == 'C':
        answer = answer.split()
        for i in range(len(answer)):
            temp = list(answer[i])

            if i == 0:
                if data[1] == 'C':
                    temp[0] = temp[0].upper()
                else: continue
            else:
                temp[0] = temp[0].upper()

            answer[i] = ''.join(temp)

        answer = ''.join(answer)
        if data[1] == 'M' and '()' not in answer: answer += '()'
    return answer

if __name__ == "__main__":

    for line in sys.stdin:
        data = list(line.split(';'))
        print(solution(data))