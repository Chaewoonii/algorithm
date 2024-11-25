# hackers rank week2, Lonely Integer

def lonelyinteger(arr):
    count_list = [0] * (max(arr) + 1)
    for n in arr:
        count_list[n] += 1
    return count_list.index(1)