# 재귀로 N부터 1까지 출력하는 함수
def reversedPrint(n):
    if n == 0:
        return
    print(n)
    return reversedPrint(n-1)


# 1부터 N까지의 합계
def recursiveSum(n, result=0):
    if n == 0:
        return result
    return recursiveSum(n-1, result + n)

if __name__ == "__main__":
    reversedPrint(5)
    print(recursiveSum(5))