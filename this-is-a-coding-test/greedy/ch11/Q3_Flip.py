# 313, 문자열 뒤집기

string = input()

string0 = len(list(filter(None, string.split('1'))))
string1 = len(list(filter(None, string.split('0'))))

print(min(string0, string1))
