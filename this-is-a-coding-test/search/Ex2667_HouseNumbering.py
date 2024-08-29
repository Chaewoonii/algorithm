#백준 2667: 단지번호붙이기

n = int(input())
houseMap = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, graph):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        global houseCount
        houseCount += 1
        graph[x][y] = 0

        dfs(x - 1, y, graph)
        dfs(x + 1, y, graph)
        dfs(x, y - 1, graph)
        dfs(x, y + 1, graph)

        return True
    return False

totalCount = 0
houseCount = 0
numberOfHouse = []
for i in range(n):
    for j in range(n):
        if dfs(i, j, houseMap):
            numberOfHouse.append(houseCount)
            totalCount += 1
            houseCount = 0

print(totalCount)
numberOfHouse.sort()
for i in numberOfHouse:
    print(i)

