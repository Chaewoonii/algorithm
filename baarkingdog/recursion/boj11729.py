# 하노이의 탑
# n개의 원판을 옮긴다

N = int(input())
count = []
# 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력
def top_of_hanoi(n, a, b):
    # basecase: n이 1개 남았다면 a에서 b로 옮겨주면 끝 / n이 0일때도 생각해보기
    if n == 1:
        count.append(f"{a} {b}")
        return

    else:
        top_of_hanoi(n-1, a, 6-a-b) # 원판 n-1 개를 a에서 6-a-b로 옮긴다.
        # n번 원판을 기둥 a에서 b로 옮긴다
        count.append(f"{a} {b}")
        # n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다
        top_of_hanoi(n-1, 6-a-b, b)

def top_of_hanoi2(n, a, b):
    if n == 0:
        return

    top_of_hanoi(n-1, a, 6-a-b) # 원판 n-1 개를 a에서 6-a-b로 옮긴다.
    count.append(f"{a} {b}")
    top_of_hanoi(n - 1, 6 - a - b, b)

top_of_hanoi2(N, 1, 3)
print(len(count))
print("\n".join(count))
