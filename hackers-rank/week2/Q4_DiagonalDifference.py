# hackers rank week2, Diagonal Difference

def diagonalDifference(arr):
    left = 0
    right = 0
    n = len(arr)
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n - 1 - i]

    return abs(left - right)
