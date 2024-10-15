# 313, 문자열 뒤집기, 정답코드

data = input()
count0 = 0 # 모두 0으로 바꾸는 경우
count1 = 1 # 모두 1로 바꾸는 경우

# 0번째 데이터가 1인 경우
if data[0] == '1':
    count0 += 1 # 1을 0으로 바꿔야 하므로 count0에 1 추가
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1  # 다음 숫자가 0에서 1로 바뀌는 경우, 0으로 만드는 그룹에 추가
        else:
            count1 += 1  # 다음 숫자가 1에서 0으로 바뀌는 경우, 1로 만드는 그룹에 추가

print(min(count0, count1))