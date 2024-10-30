# 서로소 집합을 활용한 사이클 판별
# 1. 각 간선을 호가인하며 두 노드의 루트 노드를 확인
#   1) 루트 노드가 서로 다르다면 두 노드에 대해 union 연산을 수행
#   2) 루트 노드가 서로 같다면 사이클이 발생한 것
# 2. 그래프에 포함되어있는 모든 간선에 대하여 1번 과정을 반복

# 특정 원소가 속한 집합 찾기
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선의 개수 입력
v, e = map(int, input().split())
parent = [i for i in range(v + 1)] # 부모 테이블 초기화

# 사이클 발생 여부
CYCLE = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if findParent(parent, a) == findParent(parent, b):
        CYCLE = True
        break
    else:
        unionParent(parent, a, b)

if CYCLE:
    print("사이클 발생")
else:
    print("사이클 미발생")