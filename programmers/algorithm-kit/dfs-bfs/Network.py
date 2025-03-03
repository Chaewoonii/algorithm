from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            q = deque()
            q.append((i, computers[i]))
            while q:
                idx, now = q.popleft()
                for j in range(n):
                    if now[j] == 1 and not visited[j]:
                        q.append((j, computers[j]))
                        visited[j] = 1
            visited[i] = 1
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))