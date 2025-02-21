def solution(numbers):
    numbers = list(map(str, numbers))
    # 파이썬 문자열 정렬: 첫 번째 자리 -> 두 번째 자리 -> n번째 자리: 자리 마다 비교.
    # 첫번째 자리 순 정렬: 9, 5, 3, 3, 3 -> 9, 5 고정
    # 두 번째 자리 순 정렬: 99, 55, 34, 33, 30
    # ...
    # x*3을 하지 않는다면 9, 5, 34, 30, 3 으로 정렬됨. 3의 두 번째 자리가 없으므로 제일 마지막이 된다.
    numbers.sort(key=lambda x: x*3, reverse=True) # ['999', '555', '343434', '333', '303030']
    print(numbers)
    return str(int("".join(numbers))) # 0인 경우 처리

solution([3, 30, 34, 5, 9])