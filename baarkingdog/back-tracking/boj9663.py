
#  func(0)을 호출해 0번째 행에 퀸을 배치
#  func(0)은 func(1)을 호출
#  func(n)이 호출되면 퀸 n개를 놓는데 성공했다는 의미 ➡️ cnt를 1 증가
# 퀸이 있는지 판단
# 상, 하 -> 현재 y 좌표에서 -+ | 좌, 우 -> 현재 x 좌표에서 -+
# 대각선: 우상/좌하 대각선: x+y가 같으면 대각선에 위치 (예: (4,1), (3,2), (2,3)
# 우하/좌상 대각선: x-y가 같으면 대각선에 위치 (2,2), (3,3), (4,4)
# 퀸의 목록을 외부 변수로 가지고 있고, 함수 내에서 퀸을 놓을 때 각 퀸과 대각선 혹은 열에서 만나는지 확인
# 이 방법은 놓은 모든 퀸에 대해 만나는 것이 있는지 확인해야 하기 때문에 O(N)이 추가로 필요.
# isused 변수를 쓰자. (0,0), (1,3) 의 위치에 queen이 있다.
# is_used1 = [0] * N # 열에 대응되는 값 -> 0, 3이 True
# is_used2 = [0] * (N*2-1) # 좌하우상 대각선 -> x+y: 0, 4가 True
# is_used3 = [0] * (N*2-1) # 좌상우하 대각선 -> x-y+n-1: 1,3이 True

def func(now, N, used1, used2, used3):
    if now == N:
        return 1

    count = 0
    for i in range(N): # cur행 N 번째 열에 퀸을 놓을 것이다.
        if used1[i] or used2[i + now] or used3[now - i + N - 1]: # 상하좌우, 대각선에 퀸이 있다면 넘어가
            continue
        # 상하좌우, 대각선이 퀸이 있다면 놓을 수 있어!
        used1[i] = 1
        used2[i + now] = 1
        used3[now - i + N - 1] = 1
        count += func(now + 1, N, used1, used2, used3) # 다음 열로 넘어가기
        # 요소 돌려주기
        used1[i] = 0
        used2[i + now] = 0
        used3[now - i + N - 1] = 0

    return count

if __name__ == "__main__":
    N = int(input())
    used1 = [0] * N  # 열에 대응되는 값 -> 0, 3이 True
    used2 = [0] * (N * 2 - 1)  # 좌하우상 대각선 -> x+y: 0, 4가 True
    used3 = [0] * (N * 2 - 1)  # 좌상우하 대각선 -> x-y+n-1: 1,3이 True
    result = func(0, N, used1, used2, used3)
    print(result)
