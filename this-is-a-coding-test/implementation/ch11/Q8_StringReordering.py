# 322p, 문자열 재정렬

string = list(input())
string.sort()

total = 0
for item in string:
    if item.isalpha():
        print(item, end='')
    else:
        total += int(item)

print(total)