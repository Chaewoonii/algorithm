# 내장함수
arr1 = [7, 5, 9, 0, 3, 1, 2, 6, 4, 8]

# 1 sorted()
result1 = sorted(arr1)
print(result1, arr1)

#2 list.sort()
arr1.sort()
print(arr1)

#3 튜플, 키값 지정해서 정렬
arr2 = [('사과', 2), ('바나나', 5), ('복숭아', 3), ('귤', 0)]
result2 = sorted(arr2, key=(lambda x: x[1]))
print(result2)