# 2번, 문서 제목 변경하기
#
def solution(title, date):
    answer = []
    date = [list(map(int, d.split("-"))) for d in date]

    for i in range(len(title)):
        cnt = 0
        docs = []
        for j in range(len(title)):
            if title[i] == title[j] and date[i][0] == date[j][1]: # 제목과 연도가 같을 경우
                cnt += 1
                docs.append(date[j][1]) # 달 추기

        if cnt == 1:
            answer.append(f"{date[i][0]} {title[i]}")
        elif cnt == 2:
            docs.sort()
            if docs[0] <= 6 and docs[1] > 6: # 상하반기로 나눌 수 있는 경우
                answer.append(f"{date[i][0]} {getHalf(date[i][1])} {title[i]}")
            else:
                answer.append(f"{date[i][0]} {getQuarter(date[i][1])} {title[i]}")
        else:
            answer.append(f"{date[i][0]} {getQuarter(date[i][1])} {title[i]}")

def getHalf(m):
    if m <= 6:
        return "1H"
    else:
        return "2H"

def getQuarter(m):
    if m <= 3:
        return "1Q"
    elif 4 <= m <= 6:
        return "2Q"
    elif 7 <= m <= 9:
        return "3Q"
    elif 10 <= m:
        return "4Q"