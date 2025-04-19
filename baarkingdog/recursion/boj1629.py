# 힌트
# a**n * a ** n = a ** 2n
# mod: 나머지
# 12 ** 58 % 67 = 4
# 12 ** 116 % 67 = 16

# 10 * 10 = 100 -> 12로 나눈 나머지
# a를 b번 곱한 수를 c로 나눈 나머지.
def mod(a, b, c):
    if b == 1:
        return a % c
    else:
        k = mod(a, b//2, c)
        k = k * k % c
        if b%2 == 0:
            return k
        else:
            return k * a % c # 홀수면 한 번 더 계산해준다.


