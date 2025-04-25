def cut_paper(data):
    total = sum(sum(data, []))
    if total == 0:
        return [1, 0]
    elif total == len(data) ** 2:
        return [0, 1]

    result = [0, 0]
    blocks = split_blocks(data)
    for b in blocks:
        sub = cut_paper(b)
        result = [a + b for a, b in zip(result, sub)]

    return result


def split_blocks(data):
    n = len(data) // 2
    return [
        [row[j:j + n] for row in data[i:i + n]]
        for i in range(0, len(data), n)
        for j in range(0, len(data), n)
    ]


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
print(*cut_paper(data), sep="\n")