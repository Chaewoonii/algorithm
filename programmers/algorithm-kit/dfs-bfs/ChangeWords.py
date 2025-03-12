INF = 1e9
def solution(begin, target, words):
    if target not in words:
        return 0

    min_cnt = INF
    visited = set()

    def dfs(curr, cnt):
        nonlocal min_cnt
        if curr == target:
            min_cnt = min(min_cnt, cnt)
            return

        for word in words:
            if word not in visited and canChange(curr, word):
                visited.add(word)
                dfs(word, cnt + 1)
                visited.remove(word)

    def canChange(word1, word2):
        return sum([w1 != w2 for w1, w2 in zip(word1, word2)]) == 1

    dfs(begin, 0)
    return min_cnt if min_cnt != INF else 0