def solution(numbers, target):
    global answer
    answer = 0
    def dfs(idx, n):
        global answer
        if idx == (len(numbers)):
            if n == target: answer += 1
            return

        dfs(idx + 1, n + numbers[idx])
        dfs(idx + 1, n - numbers[idx])
        return

    dfs(0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 3))