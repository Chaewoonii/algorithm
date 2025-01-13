# 370p, 가사 검색
# 2020 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def wordByLengthAndReverse(words):
    word_by_len = [[] for _ in range(100001)]
    reverse_words = [[] for _ in range(100001)]

    for word in words:
        word_by_len[len(word)].append(word)
        reverse_words[len(word)].append(word[::-1])

    for i in range(100001):
        word_by_len[i].sort()
        reverse_words[i].sort()

    return word_by_len, reverse_words

def solution(words, queries):
    answer = []
    word_by_len, reverse_words = wordByLengthAndReverse(words)

    for q in queries:
        if q.endswith("?"):
            left = bisect_right(word_by_len[len(q)], q.replace("?", "a"))
            right = bisect_left(word_by_len[len(q)], q.replace("?", "z"))
        else:
            q = q[::-1]
            left = bisect_right(reverse_words[len(q)], q.replace("?", "a"))
            right = bisect_left(reverse_words[len(q)], q.replace("?", "z"))

        answer.append(right - left)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))