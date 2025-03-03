def solution(N, number):
    if N == number: return 1

    arr = [{int(str(N) * i)} if i > 0 else set() for i in range(9)]
    print(arr)
    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i - j]:
                    arr[i].add(a + b)
                    arr[i].add(a * b)
                    arr[i].add(a - b)
                    if b > 0: arr[i].add(a // b)
        if number in arr[i]:
            print(arr)
            return i

    return -1

result = solution(3, 13)
print(result)