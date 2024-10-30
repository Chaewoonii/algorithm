# hackers rank week1, Breaking the Records
# 최고 기록, 최저 기록을 깬 횟수

def breakingRecords(scores):
    result = [0, 0]
    maximum = scores[0]
    minimum = scores[0]

    for score in scores:
        if score < minimum:
            minimum = score
            result[1] += 1
        elif score > maximum:
            maximum = score
            result[0] += 1

    return result

n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)
print(' '.join([str(i) for i in result]))
