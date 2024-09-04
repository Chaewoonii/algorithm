# 360p, q24-안테나, 정렬

n = int(input())
houses = list(map(int, input().split()))

houses.sort() # 1 5 7 9

#중간값을 출력: 정렬 후 중간 인덱스를 계산하여 출력, 인덱스를 2로 나눈 몫이 중간값.
print(houses[(n - 1) // 2])


'''
antenna = []
distance = 999999999
for i in range(max(houses)):
    dist = sum(map(lambda x: abs(x-i), houses))
    antenna.append(dist)

print(antenna.index(min(antenna)))
'''