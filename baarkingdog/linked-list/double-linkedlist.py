# 이중 연결리스트
from ast import NodeVisitor


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터

# 연결리스트의 노드를 따로 리스트에 저장하는게 나을듯.
class DoubleLinkedList:
    def __init__(self):
        self.head = DoublyNode(-1)
        self.head.prev = -1

    # 처음에 새로운 노드 삽입
    def addHead(self, data):
        node = DoublyNode(data)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    # 끝에 새로운 노드 삽입
    def add(self, data):
        curr = self.head
        node = DoublyNode(data)
        while curr:
            if curr.next is None:
                curr.next = node
                node.prev = curr
                break
            curr = curr.next

    def delete(self, node: DoublyNode):
        node.prev = node.next
        node.next.prev = node.prev

    def search(self, to_find):
        curr = self.head.next
        while curr:
            if curr.data == to_find:
                return curr
            curr = curr.next

    def moveForward(self, curr=None):
        if curr is None:
            curr = self.head.next
        while curr:
            print(curr.data, end=" ")
            if curr.next is None:
                break
            curr = curr.next
        print()
        return curr

    # 특정 노드에서 역방향 탐색
    def moveBackward(self, node:DoublyNode):
        while node:
            if node.prev == -1:
                break
            print(node.data, end=" ")
            node = node.prev
        print()
        return node # 첫 번째 요소 반환


if __name__ == "__main__":
    # 노드 생성 예시
    dnode1 = DoublyNode(1)
    dnode2 = DoublyNode(2)

    dnode1.next = dnode2  # dnode1이 dnode2를 가리키도록 설정
    dnode2.prev = dnode1  # dnode2가 dnode1을 가리키도록 설정

    dl = DoubleLinkedList()
    for i in range(10):
        dl.add(i)

    # 앞에 추가
    dl.addHead(10)

    # 정방향 탐색
    last = dl.moveForward()

    # 역방향 탐색
    dl.moveBackward(last)

    # 특정 위치에서 정방향 탐색
    node = dl.search(3)
    dl.moveForward(node)

    # 특정 위치에서 역방향 탐색
    node = dl.search(6)
    dl.moveBackward(node)




