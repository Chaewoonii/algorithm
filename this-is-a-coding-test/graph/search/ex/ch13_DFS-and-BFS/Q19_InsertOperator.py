# 349p, 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# 시간초과, itertools product 사용해보기
# 브루트포스, 백트래킹

from itertools import permutations

def getOperatorCombi(operator_data):
    plus = [0] * operator_data[0]
    minus = [1] * operator_data[1]
    multi = [2] * operator_data[2]
    div = [3] * operator_data[3]
    operators = plus + minus + multi + div
    return list(permutations(operators, sum(operator_data)))

def calculate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == 0:
            result += numbers[i + 1]
        elif operators[i] == 1:
            result -= numbers[i + 1]
        elif operators[i] == 2:
            result *= numbers[i + 1]
        elif operators[i] == 3:
            if result < 0:
                result = int(result / numbers[i + 1])
            else:
                result = result // numbers[i + 1]
    return result

def insertOprerator(numbers, operator_data):
    min_value = 9999999999
    max_value = -9999999999
    combi = getOperatorCombi(operator_data)

    for item in combi:
        min_value = min(min_value, calculate(numbers, item))
        max_value = max(max_value, calculate(numbers, item))

    return max_value, min_value

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    operator_data = list(map(int, input().split()))
    max_value, min_value = insertOprerator(numbers, operator_data)
    print(max_value)
    print(min_value)