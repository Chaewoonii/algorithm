N, S = map(int, input().split())
arr = list(map(int, input().split()))
# 원소가 n개인 집합에서 부분집합의 개수는 2**n
# i번째 수를 더할지 말지 정하고 i+1번째 수를 정하러 한 단계 더 들어간다

# length: 현재 부분수열의 크기
# tot: 현재 부분수열의 합
def func(now, tot):
    if now == N: # 모든 요소를 다 사용한 경우 종료
        if tot == S: # 합계가 S와 같다면
            return 1
        return 0

    count = 0
    count += func(now + 1, tot) # 현재 값을 선택하지 않은 경우
    count += func(now + 1, tot + arr[now]) # 현재 값을 선택한 경우

    return count

result = func(0, 0)
if S == 0: result -= 1 # 공집합은 제외하므로, s가 0일땐 하나 빼줘야 한다.
print(result)