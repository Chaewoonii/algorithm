# hackers rank week1, Sparse Arrays
# strings에 있는 queries 갯수 구하기

def matchingStrings(strings, queries):
    result = [0] * len(queries)
    for item in strings:
        for i in range(len(queries)):
            if item == queries[i]:
                result[i] += 1
    return result
