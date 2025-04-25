def quad_tree(data):
    total = sum(sum(data, []))
    if len(data) == 1:
        return str(data[0][0])
    elif total == 0:
        return "0"
    elif total == len(data) ** 2:
        return "1"

    result = []
    blocks = split_blocks(data)
    for b in blocks:
        sub = quad_tree(b)
        result.append(sub)
    return "(" + "".join(result) + ")"


def split_blocks(data):
    n = len(data) // 2
    return [
        [row[j:j + n] for row in data[i:i + n]]
        for i in range(0, len(data), n)
        for j in range(0, len(data), n)
    ]

N = int(input())
data = [list(map(int, list(input()))) for _ in range(N)]
result = quad_tree(data)
print(result)