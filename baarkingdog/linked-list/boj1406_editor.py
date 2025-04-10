import sys


class Node:
    def __init__(self, char=None):
        self.char = char
        self.prev = None
        self.next = None


input = sys.stdin.readline

# 더미 노드 생성
head = Node()
tail = Node()
head.next = tail
tail.prev = head

# 초기 문자열 입력
cursor = tail  # 커서는 항상 현재 위치 '앞에' 삽입되도록 tail에 위치
for char in input().rstrip():
    new_node = Node(char)
    new_node.prev = cursor.prev
    new_node.next = cursor
    cursor.prev.next = new_node
    cursor.prev = new_node

# 명령 처리
for _ in range(int(input())):
    command = input().split()

    if command[0] == 'L':
        if cursor.prev != head:
            cursor = cursor.prev
    elif command[0] == 'D':
        if cursor != tail:
            cursor = cursor.next
    elif command[0] == 'B':
        if cursor.prev != head:
            to_remove = cursor.prev
            to_remove.prev.next = cursor
            cursor.prev = to_remove.prev
    elif command[0] == 'P':
        new_node = Node(command[1])
        new_node.prev = cursor.prev
        new_node.next = cursor
        cursor.prev.next = new_node
        cursor.prev = new_node

# 결과 출력
result = []
node = head.next
while node != tail:
    result.append(node.char)
    node = node.next

print(''.join(result))
