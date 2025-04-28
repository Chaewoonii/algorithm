# boj15649, N과 M
def boj15649():
    N, M = map(int, input().split())
    def back_tracking(arr, used):
        if len(arr) == M:
            print(*arr, sep=" ")
            return

        for i in range(1, N + 1):
            if not used[i]:
                arr.append(i)
                back_tracking(arr, used)
                arr.pop()

    back_tracking([], [False] * (N + 1))

if __name__ == "__main__":
    boj15649()