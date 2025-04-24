def cut_paper(data):
    if len(data) == 1 or is_uniform(data):
        return get_counter(data[0][0])

    result = [0, 0, 0]
    for block in split_blocks(data):
        sub = cut_paper(block)
        result = [a + b for a, b in zip(result, sub)]
    return result

def is_uniform(data):
    val = data[0][0]
    return all(n == val for row in data for n in row)

def get_counter(val):
    if val == -1:
        return [1, 0, 0]
    elif val == 0:
        return [0, 1, 0]
    elif val == 1:
        return [0, 0, 1]

def split_blocks(data):
    n = len(data) // 3
    return [
        [row[j:j+n] for row in data[i:i+n]]
        for i in range(0, len(data), n)
        for j  in range(0, len(data), n)
    ]

# 입력 처리
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(*cut_paper(data), sep='\n')
