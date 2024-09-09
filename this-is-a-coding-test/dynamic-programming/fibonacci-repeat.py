# 피보나치 수열 - 반복문 활용
# DP 보텀업 방식: 작은 문제부터 차근차근 답을 도출

n = int(input())
fiboNums = [0, 1, 1] + ([0] * (n - 2)) # DP 테이블 초기화

for i in range(3, n + 1):
    fiboNums[i] = fiboNums[i - 1] + fiboNums[i - 2]

print(fiboNums[n])
print(fiboNums)