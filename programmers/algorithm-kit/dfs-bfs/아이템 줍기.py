# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    metrix = getPath(rectangle)
    visited = [[0] * 102 for _ in range(102)]

    cx, cy, ix, iy = map(lambda x: x * 2, [characterX, characterY, itemX, itemY])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(cx, cy)])
    visited[cx][cy] = 1 # 방문 처리
    shortest = 0
    while q:
        x, y = q.popleft()
        if x == ix and y == iy:
            shortest = visited[x][y] // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if metrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return shortest

def getPath(rectangle):
    metrix = [[-1] * 102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    metrix[i][j] = 0

                elif metrix[i][j] != 0:
                    metrix[i][j] = 1

    return metrix

if __name__ == "__main__":
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))