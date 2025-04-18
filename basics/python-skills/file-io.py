# 파이썬으로 파일 읽고 쓰기
# open 옵션: r-읽기, w-쓰기, a-추가(마지막에 새로운 내용 추가)


directory = "./resources" # 파일 경로
fileName = "test.txt" # 파일 이름

# 파일 쓰기
file = open(f"{directory}/{fileName}", 'w') # 파일 읽어오기, 쓰기모드
for i in range(1, 11):
    txt = f"{i}번째 줄 입니다.\n"
    file.write(txt)

file.close()

# 파일 읽기
file = open(f"{directory}/{fileName}", 'r')
line = file.readline()
log = ""
while True:
    line = file.readline()
    if not line: break
    log += line
file.close()
print(log)

