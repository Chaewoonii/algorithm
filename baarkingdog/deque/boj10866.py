import sys
from collections import deque

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    op = input().rstrip().split()
    if op[0] == "push_front":
        q.appendleft(op[1])

    elif op[0] == "push_back":
        q.append(op[1])

    elif op[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif op[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)

    elif op[0] == "size":
        print(len(q))

    elif op[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif op[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif op[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
