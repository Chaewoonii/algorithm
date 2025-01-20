def addMonths(date, add_month):
    year, month, day = map(int, date.split("."))

    day -= 1
    if day <= 0:
        day = 28
        month -= 1

        if month <= 0:
            month = 12
            year -= 1

    month += add_month
    while month > 12:
        month -= 12
        year += 1

    return year, month, day


def isDelete(today, y, m, d):
    ty, tm, td = map(int, today.split("."))

    '''
    유효기간이 지난 경우: today > 유효기간: 오늘 날짜가 유효기간보다 <큰> 경우
    1. 오늘 연도 > 유효기간 연도
    2. 오늘 연도 = 유효기간연도, 오늘 month > 유효기간 month
    3. 오늘 연도 = 유효기간 연도, 오늘 month = 유효기간 month, 오늘 날짜 > 유효기간 날짜
    '''
    if ty > y: return True
    elif ty == y and tm > m: return True
    elif ty == y and tm == m and td > d: return True
    else: return False


def solution(today, terms, privacies):
    t_dic = {}

    for i in range(len(terms)):
        term, month = terms[i].split()
        t_dic[term] = int(month)

    result = []
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        y, m, d = addMonths(date, t_dic[term])
        if isDelete(today, y, m, d):
            result.append(i + 1)

    return result

if __name__ == "__main__":
    result = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    print(result)

    result2 = solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
    print(result2)