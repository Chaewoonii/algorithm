# 윷놀이
# 도(3) 개(2) 걸(1) 윷(0) 모(5)
data = ["D", "C", "B", "A", "E"]

for _ in range(3):
    print(data[sum(list(map(int, input().split())))])