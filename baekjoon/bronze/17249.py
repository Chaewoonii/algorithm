# 태보태보 총난타
data = input()
print(data[:data.index('(')].count('@'), end=" ")
print(data[data.index(')'):].count('@'))