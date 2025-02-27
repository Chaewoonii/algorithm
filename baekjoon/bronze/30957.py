n = int(input())
data = input()
count = {"B":0, "S":0, "A":0}
for d in data:
    count[d] += 1

if sum(count.values()) % 3 == 0:
    print("SCU")
else:
    for k, v in count.items():
        if v == max(count.values()):
            print(k, end="")


# N = int(input())
# B, S, A = map(list(input()).count, 'BSA') # 문자열 'BSA' 가 입력데이터에 몇 번 들어가있는지 계산
## B, S, A = map([*open(0)][1].count, 'BSA')
# print(''.join(i*(max(B,S,A)==eval(i)) for i in 'BSA').replace('BSA', 'SCU'))
# max(B,S,A)==eval(i) eval(): 문자열을 수식으로 바꿔 계산
# max(B,S,A)==eval("B") -> max(B, S, A) == B
# -> True 면 조건식(max, eval)이 1, i * 1 -> 'B' * 1 -> B
# -> False 면 조건식이 0, i * 0 -> 'A' * 0 -> None
# 만약에 BSA 모두 최댓값이라 'BSA' 이면 'SCU'로 replace