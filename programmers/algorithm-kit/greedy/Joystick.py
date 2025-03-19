# 소마 2차 1번문제와 비슷
def solution(name):
    A = ord('A')
    Z = ord('Z')
    change_alphabet = 0
    cursor = len(name) - 1  # 커서 움직이는 횟수

    for i, apb in enumerate(name):
        change_alphabet += min(ord(apb) - A, Z - ord(apb) + 1)  # A에서 오른쪽 이동, A에서 왼쪽이동 중 최솟값

        # 연속된 A의 값 찾기
        nxt = i + 1  # 다음 A가 아닌 값의 인덱스
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1

        # 커서를 왼쪽으로 이동 vs 오른쪽으로 이동
        # 0123456789
        # BABBAAAAAB
        # 1. 가장 긴 A의 왼쪽부터 바꾸기: 현재 위치까지 온 후(i) 다시 되돌아가서(i) 마지막 위치(len(name))에서 nxt까지 이동
        # 2. 가장 긴 A의 오른쪽부터 바꾸기: 마지막 위치부터 nxt로 이동 후 다시 마지막으로 되돌아가서 첫 번째 위치에서 i로 이동
        cursor = min(cursor,
                     i * 2 + (len(name) - nxt),
                     (len(name) - nxt) * 2 + i)

    return change_alphabet + cursor


