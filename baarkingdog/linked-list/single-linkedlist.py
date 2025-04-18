# 단일 연결리스트
class Node:
    def __init__(self, data):
        self.data = data # 노드가 저장할 데이터
        self.next = None # 다음 노드를 가리키는 포인터

class SinglyLinkedList:
    def __init__(self):
        self.head = Node(-1) # 리스트의 시작을 가리키는 포인터 0번지는 특별히 -1

    # 연결 리스트의 끝에 새로운 노드 삽입
    def add(self, data):
        curr = self.head
        while curr:
            if curr.next is None:
                curr.next = Node(data)
                break
            curr = curr.next

    # 연결 리스트의 처음에 새 노드 추가
    def insertHead(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node

    # 연결 리스트의 값 출력
    def traverse(self):
        node = self.head.next
        while node:
            print(node.string, end =" ")
            node = node.next
        print()

    # 값 탐색
    def search(self, to_find):
        curr = self.head.next
        while curr:
            if curr.string == to_find:
                return curr
            curr = curr.next

    # 특정 값 (첫 번째 값) 삭제 : 삽입/삭제가 불편해서 이중 연결리스트가 나음...
    def delete(self, to_delete):
        prev = self.head # 이전 노드
        curr = self.head.next # 현재 노드
        while curr:
            if curr.string == to_delete:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next


if __name__ == "__main__":
    # 노드 생성 예시
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2 # 노드 1이 노드 2를 가리키도록 설정
    print(node1.next.data) # 2
    print(node2.next) # None

    # 연결리스트 생성 및 테스트
    sl = SinglyLinkedList()
    for i in range(10):
        sl.add(i)

    # 연결리스트 방문
    sl.traverse()

    # 처음에 새 노드 추가
    sl.insertHead(10)
    sl.traverse()

    # 값 탐색
    print(sl.search(6).next.string) # 7

    # 값 삭제
    sl.delete(6) # 중간 값
    sl.delete(9) # 마지막 값
    sl.delete(10) # 첫 번째 값
    sl.traverse()