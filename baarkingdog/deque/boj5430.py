from collections import deque

for _ in range(int(input())):
    P = input()
    N = int(input())
    arr = list(input()[1:-1].split(','))

    if N == 0:
        q = deque()
    else:
        q = deque(arr)

    reverse = False
    for p in P:
        if p == "R":
            reverse = not reverse
        elif p == "D":
            if not q:
                print("error")
                break

            if reverse: q.pop()
            else: q.popleft()
    else:
        if reverse: q.reverse()
        print('[' + ",".join(q) + "]")