# 메모이제이션(memoization)(캐싱, caching)을 통한 최적화
# 한 번 구한 정보를 리스트에 저장, 연산 최소화
# DP, 탑다운 방식: 큰 문제를 해결하기 위해 작은 문제를 호출

n = int(input())

#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
# [0, 1, 1]
#   - 0: 인덱스는 0부터 시작하므로 n번째 원소에 접근하기 위해서는 list[n-1] 과 같이 코드를 작성해야함
#        편의상 list[n]으로 접근하기 위해 0번째 인덱스에 0을 삽입, list[n]으로 접근
#   - 1, 1: 피보나치 수열의 첫 번째, 두 번째 수는 1이므로 미리 초기화. (연산 횟수 줄이기)
fiboNums = [0, 1, 1] + ([0] * (n - 2))

def fiboMemo(n):
    # 아직 계산하지 않은 문제일 경우 점화식에 따라 피보나치 결과 반환
    if fiboNums[n] == 0 and n > 2:
        fiboNums[n] = fiboMemo(n - 1) + fiboMemo(n - 2)

    return fiboNums[n]

print(fiboMemo(n))
print(fiboNums)