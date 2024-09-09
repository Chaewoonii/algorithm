# 피보나치 수열 / 단순 재귀. O(2n^), n이 30을 넘을 경우 10억 가량의 연사을 수행 해야함. 답 도출 불가..
# dynamic-programming 의 메모이제이션을 통하여 최적화 (fibonacci-memo.py)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 1 1 2 3 5 8 13 21 34 55
print(fibonacci(10))