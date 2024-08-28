'''
유클리드 호제법
정수 A, B에 대하여 A > B일 때,
A와 B의 최대공약수(GCD)는
A를 B로 나눈 나머지 r과 B의 최대공약수와 같다

int num1, num2 (num1 > num2)
r = num1 % num2
num1, num2 GCD == num2, r GCD
'''

# 유클리드 호제법 재귀함수 구현

def gcd(a, b):
    r = a % b
    if r == 0: # r이 0이면, 즉, a가 b의 배수이면 b를 반환
        return b
    else:
        return b % gcd(b, r)
