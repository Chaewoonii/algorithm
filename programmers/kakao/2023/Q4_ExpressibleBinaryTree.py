
# 이진탐색 알고리즘, 포화이진트리 구성
def getSaturatedBinaryTree(binary, start, end):
    if abs(start - end) <= 1: return binary

    root = (start + end) // 2 # 중간점, root 노드

    # root 를 기준으로 왼쪽 서브트리 구성, 짝수이면 왼쪽에 0을 넣는다.
    if len(binary[start:root]) % 2 == 0:
        return getSaturatedBinaryTree(binary[:start] + "0" + binary[start:], start, root - 1)

    # root 를 기준으로 오른쪽 서브트리 구성, 짝수이면 오른쪽에 0을 넣는다.
    elif len(binary[root:end]) % 2 == 0:
        return getSaturatedBinaryTree(binary[:end] + "0" + binary[end:], root + 1, end)

    else:
        return binary

# 이진 탐색, root 가 0으로 나올 경우 False
def check_subtree(subtree):
    if not subtree: return True

    root = len(subtree) // 2

    if subtree[root] == '0' and ('1' in subtree[:root] or '1' in subtree[root + 1:]):
        return False

    return check_subtree(subtree[:root]) and check_subtree(subtree[root + 1:])

def solution(numbers):
    answer = []

    for num in numbers:
        binary = bin(num)[2:]
        s_binary = getSaturatedBinaryTree(binary, 0, len(binary))
        if check_subtree(s_binary) == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer

if __name__ == "__main__":
    print(solution([7, 42, 5])) # ToDo: 왜 1, 0, 0 나오는지 디버김
    print(solution([63, 111, 95]))
