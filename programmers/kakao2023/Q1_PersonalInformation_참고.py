# year, month에 day의 단위인 28을 곱하는 방식으로 날짜를 환산하여 계산

def to_days(date):
    year, month, day = map(int, date.split("."))
    # 연도 * 12달 * 28일, month * 28일, 날짜
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    # A 6 형태이므로, term는 길이 3~4의 문자열(idx: 0~3). 따라서, 0번째 문자는 약관이름, 2~3번째 문자는 보관기간
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire