# 217p, 1로 만들기

x = int(input())
dpTable = [0] * 30001 # 수의 범위가 1부터 30,000 이므로 30,001

# 바텀업 방식, 2부터 x까지
# 각각의 수에 대한 최적 해를 찾음
# 예를 들어, x가 6이면 x-1인 5, x/2인 3, x/3인 2 중 연산 횟수 최솟값을 선택
# 2는 x-1인 1, x/2인 1. 1을 호출함 // 연산횟수 1회, 3, 5도 마찬가지
#       x =     1  2  3  4  5  6
# dpTable = [0, 0, 1, 1, 2, 1, 2]
# dpTable[6] = min(dpTable[5], dpTable[3], dpTable[2]) + 1 -> min(1, 1, 1) + 1 -> 1+1 -> 2
# + 1: 연산을 이미 한 번 수행했으므로 1을 더해줌
# 마찬가지로 x가 7일땐 min(dpTable[6]) + 1
# 7은 2, 3, 5로 나뉠 수 없으므로 dpTable[6]이 호출되고, 값은 2 + 1, 3이 된다.
# 이렇게 원하는 수가 될 때까지 dpTable에 값을 저장하고 호출
for i in range(2, x + 1):
    # 현재 수에서 1을 빼는 경우
    dpTable[i] = dpTable[i - 1] + 1 #dpTable[6] = dpTable[5] + 1 = 2

    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dpTable[i] = min(dpTable[i], dpTable[i // 2] + 1) # min(dpTable[6], dpTable[3] + 1), min(2, 2) = 2

    # 현재 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dpTable[i] = min(dpTable[i], dpTable[i // 3] + 1) # min(dpTable[6], dpTable[2] + 1), min(2, 2) = 2

    # 현재 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dpTable[i] = min(dpTable[i], dpTable[i // 5] + 1) # min(dpTable[6], dpTable[5] + 1), min(2, 2) = 2

print(dpTable[:x+1])
print(dpTable[x])
