# hackers rank
# 플러스 마이너스

def plusMinus(arr):
    result = [0, 0, 0]
    for item in arr:
        if item > 0:
            result[0] += 1
        elif item < 0:
            result[1] += 1
        elif item == 0:
            result[2] += 1

    for i in result:
        print(f"{i / len(arr):.7f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
