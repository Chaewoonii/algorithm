INF = 1e9

def solution(arr):
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    N = len(nums)
    min_dp = [[INF] * N for _ in range(N)]
    max_dp = [[-INF] * N for _ in range(N)]

    for i in range(N):
        min_dp[i][i] = max_dp[i][i] = nums[i] # 자기자신 초기화

    #부분배열의 크기
    # -> 크기가 size인 부분배열(nums[i:j])을 계산하여 최댓값(max_dp[i][j) 및 최솟값(min_dp[i][j) 저장
    # 연산자는 i부터 j 사이에 있는 것을 가져옴
    # 연산자가 덧셈이라면 최댓값 = 최대+최대, 최솟값 = 최소+최소
    # 연산자가 뺄셈이라면 최댓값 = 최대-최소, 최솟값 = 최소-최대
    for size in range(1, N):
        for i in range(N - size): # 부분배열 시작지점
            j = i + size # 부분배열 끝점
            for k in range(i, j): # 연산자 가져오기
                if operators[k] == ("+"): # 덧셈 연산
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = max(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = max(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])

    return max_dp[0][-1] # 전체 배열(부분배열 0부터 마지막 까지) 중 최댓값을 가져옴


# 재귀함수 방식, 시간초과
def calculate(arr):
    result = []
    if len(arr) <= 3: return [eval("".join(arr))]

    for i, curr in enumerate(arr):
        if curr.isdigit(): continue

        left = calculate(arr[:i])
        right = calculate(arr[i+1:])

        for l in left:
            for r in right:
                if curr == "+":
                    result.append(l + r)
                elif curr == "-":
                    result.append(l - r)
                elif curr == "*":
                    result.append(l * r)
    return result

if __name__ == "__main__":
    solution(["1", "-", "3", "+", "5", "-", "8"])