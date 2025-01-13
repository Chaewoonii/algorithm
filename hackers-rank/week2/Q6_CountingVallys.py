# hackers rank week2, Counting Vallys
# 계곡의 수 구하기

def countingValleys(steps, path):
    location = 0
    vallys = 0
    for p in path:
        if p == "U":
            location += 1
            if location == 0:
                vallys += 1
        elif p == "D":
            location -= 1

    return vallys