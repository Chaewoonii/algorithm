def get_stars(n):
    if n == 1:
        return ["*"]

    stars = get_stars(n // 3)
    result = []

    for s in stars:
        result.append(s*3)

    for s in stars:
        result.append(s + " "*(len(s)) + s)

    for s in stars:
        result.append(s*3)

    return result

n = int(input())
print('\n'.join(get_stars(n)))