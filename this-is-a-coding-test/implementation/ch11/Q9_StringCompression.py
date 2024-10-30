# 323p, 문자열 압축
# 2020 카카오 신입 공채
# programmers.co.kr/learn/courses/30/lessons/60057

def solution(string):
    answer = len(string)
    half = int(len(string) / 2)

    for i in range(1, half + 1):
        compressed_string = ''
        sliced_string = string[:i]
        cnt = 1

        for j in range(i, len(string), i):
            compare = string[j:j+i]
            if sliced_string == compare:
                cnt += 1
            else:
                compressed_string += str(cnt) + sliced_string if cnt > 1 else sliced_string
                sliced_string = compare
                cnt = 1

        compressed_string += str(cnt) + sliced_string if cnt > 1 else sliced_string
        answer = min(answer, len(compressed_string))

    return answer

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))