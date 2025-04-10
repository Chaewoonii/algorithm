from collections import deque
# 투포인터 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42885#

def solution(people, limit):
    if len(people) == 1: return 1
    people.sort()
    people = deque(people)
    boat = 0

    while len(people) >= 2:
        left = people.popleft()
        right = people.pop()

        if left + right > limit:
            people.appendleft(left)

        boat += 1

    if people: boat += 1

    return boat