# 298p, 팀 결성


def unionTeam(parent, a, b):
    a = findTeam(parent, a)
    b = findTeam(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findTeam(parent, x):
    if parent[x] != x:
        parent[x] = findTeam(parent, parent[x])
    return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(m):
    operation, a, b = map(int, input().split())

    if operation:
        parentA = findTeam(parent, a)
        parentB = findTeam(parent, b)

        if parentA == parentB: print("YES")
        else: print("NO")

    else:
        unionTeam(parent, a, b)
