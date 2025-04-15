import sys
input = sys.stdin.readline
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = Node(None)
tail = Node(None)
head.next = tail
tail.prev = head

cursor = tail  # 커서는 마지막에 위치
for data in input().rstrip():
    node = Node(data)
    node.prev = cursor.prev  # 커서 앞에 삽입
    node.next = cursor
    cursor.prev.next = node
    cursor.prev = node

for _ in range(int(input())):
    op = input().split()
    if op[0] == "L" and cursor.prev != head:
        cursor = cursor.prev

    elif op[0] == "D" and cursor.next != tail:
        cursor = cursor.next

    elif op[0] == "B" and cursor.prev != head:
        to_delete = cursor.prev
        to_delete.prev.next = cursor
        cursor.prev = to_delete.prev

    elif op[0] == "P":
        add = Node(op[1])
        add.prev = cursor.prev
        add.next = cursor
        cursor.prev.next = add
        cursor.prev = add

result = []
node = head.next
while node != tail:
    result.append(node.data)
    node = node.next

print("".join(result))