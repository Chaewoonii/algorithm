# 수열을 이용한 답안

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort()
maxNum = arr[len(arr) - 1]
sndNum = arr[len(arr) - 2]

# 가장 큰 수가 k번 등장하고, 두 번째로 큰 수가 1회 등장한다. 따라서 수열의 크기는 k+1이다.
maxNumCnt = int(m / (k + 1)) * k # arr에서 가장 큰 수가 등장하는 횟수. 총 m회 더해야하므로 m을 k+1로 나눈다.
                                 # k는 연속하여 더할 수 있는 횟수이므로, 나눈 값(몫)에 k를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
                                 # 예를 들어, m = 9, k = 3라고 할 때, int(9 / 4) * 3 = 6

maxNumCnt += m % (k + 1) # m을 k + 1로 나눈 나머지 만큼 가장 큰 수가 다시 등장할 수 있으므로 더해준다. 9 % 4 = 1
                         # 가장 큰 수는 7회 등장한다.
                         # 따라서 두번째로 큰 수는 9(m)에서 가장 큰 수가 등장한 횟수를 뺀 수 만큼 등장한다. 9-7 = 2
result = maxNum * maxNumCnt + sndNum * (m - maxNumCnt)
print(result)