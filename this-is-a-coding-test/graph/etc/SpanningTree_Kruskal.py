'''
- 최소 신장 트리 알고리즘: 크루스칼 알고리즘
- 신장 트리: 하나의 그래프가 있을 때, 모든 노드를 포함하면서 싸이클이 존재하지 않는 부분 그래프
- 최소 신장 트리 알고리즘: 다양한 경우의 신장 트리 중 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
- 크루스칼 알고리즘(Kruskal Algorithm): 대표적인 최소 신장 트리 알고리즘. 그리디 알고리즘으로 분류

** 구현과정 **
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 긴선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
  1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
  2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
3. 모든 간선에 대하여 2번의 과정을 반복
'''

# 크루스칼 알고리즘 소스코드

# 특정 원소가 속한 집합 찾기
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

edges = [] # 모든 간선의 정보를 담을 리스트
result = 0 # 최종 비용이 저장될 변수

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # cost가 첫 번째 원소: 비용 순으로 정렬하기 위함
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b): # 사이클이 발생하지 않는 경우: a와 b의 부모 노드가 다른 경우
        unionParent(parent, a, b)
        result += cost

print(result)