'''
h-index: h편 이상의 논문이 h번 이상 인용됨
예시:
    - 인용 횟수: 30, 28, 15, 10, 5, 4, 1, 0
    - 논문 편수:  1,  2,  3,  4, 5, 6, 7, 8
    ---> 5 편 이상의 논문이 5회 이상 인용됨. h-index는 5
오름차순으로 정렬할 경우:
    - 인용 횟수: 0, 1, 4, 5, 10, 15, 28, 30
    - 논문 편수: 1, 2, 3, 4,  5,  6,  7,  8
    ----> h-index를 찾을 수 없음

'''

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer += 1
        else:
            break

    return answer