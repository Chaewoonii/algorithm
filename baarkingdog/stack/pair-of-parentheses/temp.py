from timeit import timeit

# 조건에 포함 되지 않는 경우
print(timeit("s='1'; s == '(' or s == ')' or s == '[' or s == ']'"))
print(timeit("s='1'; s in '()[]'"))
print(timeit("s='1'; s in ['(',')','[',']']"))

# 조건에 포함 되는 경우
print(timeit("s=']'; s == '(' or s == ')' or s == '[' or s == ']'"))
print(timeit("s=']'; s in '()[]'"))
print(timeit("s=']'; s in ['(',')','[',']']"))

