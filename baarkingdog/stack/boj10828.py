class Stack:
    def __init__(self):
        self.pos = 0
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        self.pos += 1

    def pop(self):
        if self.pos > 0:
            self.pos -= 1
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return self.pos

    def empty(self):
        return 1 if self.pos == 0 else 0

    def top(self):
        return self.stack[self.pos - 1] if self.pos > 0 else -1


stack = Stack()
for _ in range(int(input())):
    op = input().split()
    if op[0] == "push":
        stack.push(op[1])

    elif op[0] == "pop":
        print(stack.pop())

    elif op[0] == "size":
        print(stack.size())

    elif op[0] == "empty":
        print(stack.empty())

    elif op[0] == "top":
        print(stack.top())

