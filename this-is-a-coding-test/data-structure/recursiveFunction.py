# 재귀함수 - 팩토리얼 예제

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))