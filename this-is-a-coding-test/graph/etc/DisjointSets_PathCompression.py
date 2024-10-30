# 서로소 집합(Disjoint Sets): 공통 원소가 없는 두 집합
# 서로소 집합 알고리즘: 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 서로소 집합 자료구조는 union과 find 두 개의 연산으로 조작할 수 있으며, union-find 자료구조라고 불리기도 함
# - union(합치기): 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# - find(찾기): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# findParent 함수를 '경로 압축(Path Compression)' 기법을 통해 최적화
# 경로 압축 기법: find 함수를 재귀적으로 호출한 뒤, 부모 테이블값을 바로 갱신
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b: # 더 작은 수를 부모 노드로 설정
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블: 부모를 자기 자신으로 초기화
parent = [i for i in range(v + 1)]

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    unionParent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(findParent(parent, i), end=' ')

print()

# 부모 테이블 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
