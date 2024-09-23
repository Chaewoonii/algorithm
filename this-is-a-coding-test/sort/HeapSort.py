# 힙 정렬: 우선순위 큐 이용
# 우선순위 큐: 우선순위가 가장 높은 데이터를 가장 먼저 삭제
# 최소 힙: 값이 작은 데이터가 먼저 삭제
# 최대 힙: 값이 큰 데이터가 먼저 삭제
# 파이썬의 heapq 라이브러리는 최소 힙을 기반으로 함
import heapq

# 오름차순 힙 정렬
def heapsort_asc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 내림차순 힙 정렬
def heapsort_desc(iteralbe):
    h = []
    result = []
    for value in iteralbe:
        heapq.heappush(h, -value) # 내림차순 정렬을 위해 값을 음수처리
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 음수처리 되어있기 때문에 다시 -를 하여 양수 처리
    return result

iter = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
asc = heapsort_asc(iter)
desc = heapsort_desc(iter)
print(asc)
print(desc)
