# 완전 탐색

from itertools import product

def solution(users, emoticons):
    max_subscribers = 0
    max_sales = 0
    dc_rate = [0.9, 0.8, 0.7, 0.6]
    dc_combi = product(dc_rate, repeat=len(emoticons))

    # 모든 경우의 수
    for dc in dc_combi:
        subscriber = 0
        total_sales = 0
        for u in range(len(users)):
            # 유저마다 판매량 계산
            sales = 0
            for e in range(len(emoticons)):
                if (100 - (dc[e] * 100)) >= users[u][0]: # 최소 할인율을 넘는 경우에만 구매
                    sales += emoticons[e] * dc[e]

            if sales >= users[u][1]: # 이모티콘 구매가가 유저 예산보다 넘어서면 구독자 증가
                subscriber += 1
            else:
                total_sales += sales

        if subscriber > max_subscribers or (subscriber == max_subscribers and total_sales > max_sales):
            max_subscribers = subscriber
            max_sales = total_sales

    return [max_subscribers, int(max_sales)]

if __name__ == "__main__":
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900, 5900, 2300, 7800, 9900]))