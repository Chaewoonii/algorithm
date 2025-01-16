# 그리디 예제 복습

# 1, 모험가 길드
'''
5
2 3 1 2 2
'''
def advanturerGuild():
    n = int(input())
    guild = list(map(int, input().split()))
    guild.sort()

    group_count = 0
    member = 0
    for i in range(n):
        member += 1
        if member <= guild[i]:
            group_count += 1
            member = 0

    print(group_count)

# 2, 곱하기 혹은 더하기
'''
02984
567
'''
def addOrMulti():
    s = list(map(int, list(input())))

    total = s[0]
    for i in range(1, len(s)):
        total = max(total + s[i], total * s[i])

    print(total)

# 3, 문자열 뒤집기
# 001100, 001100110
def stringFilp():
    s = input()
    flip0 = [item for item in list(s.split('0')) if item != '']
    flip1 = [item for item in list(s.split('1')) if item != '']
    # print(flip0, flip1)
    print(min(len(flip0), len(flip1)))


# 4, 만들 수 없는 금액
'''
5
3 2 1 1 9
'''
def cantBeMade():
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()

    target = 1
    for c in coins:
        if target < c: break
        target += c

    print(target)



if __name__ == "__main__":
    cantBeMade()