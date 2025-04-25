li = [[1] * 3 for _ in range(3)]
print(sum(li, []))
print(sum(sum(li, [])))

li_2 = [
        [i+j for j in range(1, 4)]
        for i in range(0, 9, 3)
        ]
print(li_2) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


temp = [[i for i in range(9)] for _ in range(9)]
def split_blocks(data, volume):
    n = len(data) // volume
    return [
        [row[j:j+n] for row in data[i:i+n]]
        for i in range(0, len(data), n)
        for j  in range(0, len(data), n)
    ]

blocks = split_blocks(temp,3)
print(temp)
for t in temp:
    print(t)
for b in blocks:
    print(b)
    print("***")



arr1 = [[1, 2], [3, 4]]
arr2 = [[5, 6], [7, 8]]
sum_arr = [[a + b for a, b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]
print(sum_arr)

lili = [1, 2, 3, 4, 5]
print(*lili, sep=" ")
print(*lili, sep="\n")
print(*sum_arr, sep=" ")
print(*sum(sum_arr, []), sep=" ")

