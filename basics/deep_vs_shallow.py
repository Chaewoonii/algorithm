import copy

# 정수
a = 5
b = copy.deepcopy(a)
c = a

print(a, b, c) # 5, 5, 5
print(id(a), id(b), id(c)) # 모두 같은 주소이다.

a -= 1
print(a, b, c) # 4, 5, 5
print(id(a), id(b), id(c)) # a의 주소가 바뀜

b -= 2
print(a, b, c) # 4, 3, 5
print(id(a), id(b), id(c)) # b의 주소가 바뀜

c -= 3
print(a, b, c) # 4, 3, 2
print(id(a), id(b), id(c)) # c의 주소가 바뀜


# 리스트
a = [3, 3, 3]
b = copy.deepcopy(a)
c = a

print(id(a))
print(id(b))
print(id(c))

a[1] -= 1
print(a)
print(b)
print(c)


# 2차원 리스트
N = 3
list1 = [[N] * N] * N # 얕은 복사
list2 = [[N] * N for _ in range(N)]

for i in range(N):
    print(id(list1[i])) # 같은 주소 값을 가진다

for i in range(N):
    print(id(list2[i])) # 서로 다른 주소 값을 가진다.

# 값 변경
list1[0][1] -= 1
list2[0][1] -= 1

print(list1) # 전체 행렬의 값이 바뀐다
print(list2) # 행렬 0번 1번지의 값만 바뀐다.