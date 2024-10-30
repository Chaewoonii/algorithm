# hackers rank week1, Time Conversion
# 12시간 am, pm 포맷을 24시간 포맷으로 바꾸기

def timeConversion(s):
    flag = s[-2:]
    hour = int(s[:2])
    if flag == "PM":
        if hour == 12:
            return s[:-2]
        else:
            return str(hour + 12) + s[2:-2]

    else:
        if hour == 12:
            return "00" + s[2:-2]
        else:
            return s[:-2]

print(timeConversion("07:05:45PM"))
print(timeConversion("05:40:21AM"))
print(timeConversion("12:11:00AM"))
print(timeConversion("12:12:12PM"))
