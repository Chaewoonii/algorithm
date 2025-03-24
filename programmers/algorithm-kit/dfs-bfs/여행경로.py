# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict
def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list) # 키가 없을 경우 리스트를 자동 생성
    for a, b in tickets:
        graph[a].append(b)

    # 역순 정렬: pop 위함
    for k in graph.keys():
        graph[k].sort(reverse=True)

    answer = dfs(graph, "ICN", []) # 탐색 시작
    return answer[::-1] # 역순정렬 했으므로 뒤집어서 반환

def dfs(graph: dict, start: str, answer: list):
    while graph[start]:
        nxt = graph[start].pop()
        dfs(graph, nxt, answer)
    answer.append(start)
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))