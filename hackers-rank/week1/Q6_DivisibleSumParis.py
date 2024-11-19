# hackers rank week1, Divisible Sum Paris
# k로 나누어 떨어지는 조합의 개수 구하기

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            temp = (ar[i] + ar[j]) % k
            if temp == 0:
                count += 1
    return count

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))