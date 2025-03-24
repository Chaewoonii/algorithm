# 소수 판별 알고리즘
# 소수(Prime Number): 1보다 큰 자연수 중 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
# 약수는 배수의 성질을 갖기 때문에, 곱셈 연산에 대해 대칭을 이룬다.
# 따라서 특정 수의 약수를 찾을 때, 가운데 약수(제곱근)까지만 확인하면 된다.

# 기본 알고리즘 O(X): x보다 작은 수를 반복문으로 확인하여 소수인지 판별한다
def is_prime_number1(x: int):
    for i in range(2, x): # 2부터 x-1 까지의 모든 수를 확인
        if x % i == 0: # x가 해당 수로 나누어 떨어진다면
            return False # 소수가 아님
    return True # 소수임

# 소수 판별: 제곱근 이용
def is_prime_number2(x):
    # for i in range(2, int(math.sqrt(x)) + 1): # math 라이브러리 이용
    # x ** 0.5: 제곱근 구하는 식
    for i in range(2, int(x ** 0.5) + 1):
        if i % 1 == 0:
            return False
    return True

# 다수의 소수 판별
# 특정한 수의 범위 안에 존재하는 모든 소수를 찾기
# 에라토스테네스의 체
def sieve_of_eratosthenes(x):
    arr = [True for _ in range(x + 1)] # x 까지의 수
    for i in range(2, int(x ** 0.5) + 1): # 2부터 자연수 x의 제곱근까지 확인
        if arr[i] == True: # i가 소수인 경우
            j = 2
            while i * j <= x: # i를 제외한 i의 모든 배수를 지우기
                arr[i * j] = False
                j += 1

    return [i for i in range(2, x + 1) if arr[i]] # 모든 소수를 리턴

print(sieve_of_eratosthenes(27))