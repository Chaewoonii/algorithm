    # 남 동 북 서
dx = [0, 1, 0, -1]  # 열의 움직임
dy = [1, 0, -1, 0]  # 행의 움직임

def show_map(dummy_map):
    for m in dummy_map:
        print(m)

def change_direction(direction, c):
    if c == "L":
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

def dummy_game_start(dummy_map, movements):
    time = 0
    x, y = 1, 1
    direction = 0
    snake_location = [(x, y)]

    dummy_map[x][y] = 2
    flag = True

    while flag:
        move, c = movements.pop(0)

        for _ in range(move):
            time += 1
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 게임 지속: 뱀 머리가 벽을 만나지 않고, 몸통을 만나지 않은 경우
            if 0 < nx <= n and 0 < ny <= n and dummy_map[nx][ny] != 2:
                # 사과를 만난 경우, 뱀의 꼬리를 늘린다. 즉, 머리는 옮기고 꼬리는 남겨 두기.
                if dummy_map[nx][ny] == 1:
                    dummy_map[nx][ny] = 2
                    snake_location.append((nx, ny))

                else: # 사과를 만나지 않은 경우, 뱀을 이동(지나간 자리를 비운다)
                    dummy_map[nx][ny] = 2
                    snake_location.append((nx, ny))
                    px, py = snake_location.pop(0)
                    dummy_map[px][py] = 0

                x, y = nx, ny
                # print(time)
                # show_map(dummy_map)
            # 게임 종료: 뱀 머리가 벽을 만나거나 몸통을 만난 경우
            else:
                # print(f"time:{time} | x, y: {x}, {y} | nx, ny: {nx}, {ny}")
                flag = False
                break

        direction = change_direction(direction, c) # 이동 후 방향 전환
    return time


if __name__ == "__main__":
    # 맵 크기
    n = int(input())
    dummy_map = [[0] * (n + 1) for _ in range(n + 1)]

    # 사과 개수 및 위치 정보
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        dummy_map[a][b] = 1

    # 이동 횟수 및 방향 정보
    l = int(input())
    movements = []
        # 아래, 오른쪽, 위, 왼쪽
    for _ in range(l):
        x, c = input().split()
        movements.append((int(x), c))

    result = dummy_game_start(dummy_map, movements)
    print(result)