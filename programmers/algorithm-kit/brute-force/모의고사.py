def solution1(answers):
    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]

    for idx, student in enumerate(students):
        i = 0
        for a in answers:
            if a == student[i]:
                scores[idx] += 1

            i = i + 1 if i < len(student) - 1 else 0

    return [i + 1 for i in range(3) if scores[i] == max(scores)]
''' solution1
테스트 1 〉	통과 (0.01ms, 9.27MB)
테스트 2 〉	통과 (0.01ms, 9.25MB)
테스트 3 〉	통과 (0.01ms, 9.27MB)
테스트 4 〉	통과 (0.01ms, 9.28MB)
테스트 5 〉	통과 (0.03ms, 9.27MB)
테스트 6 〉	통과 (0.04ms, 9.27MB)
테스트 7 〉	통과 (1.88ms, 9.39MB)
테스트 8 〉	통과 (0.64ms, 9.28MB)
테스트 9 〉	통과 (3.41ms, 9.32MB)
테스트 10 〉	통과 (1.62ms, 9.3MB)
테스트 11 〉	통과 (3.68ms, 9.42MB)
테스트 12 〉	통과 (3.28ms, 9.22MB)
테스트 13 〉	통과 (0.21ms, 9.28MB)
테스트 14 〉	통과 (3.78ms, 9.34MB)
'''

# 반복문 한 번만 사용
def solution2(answers):
    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]

    for i, a in enumerate(answers):
        if a == students[0][i % len(students[0])]:
            scores[0] += 1

        if a == students[1][i % len(students[1])]:
            scores[1] += 1

        if a == students[2][i % len(students[2])]:
            scores[2] += 1

    return [i + 1 for i in range(3) if scores[i] == max(scores)]
'''solution2
테스트 1 〉	통과 (0.01ms, 9.24MB)
테스트 2 〉	통과 (0.01ms, 9.23MB)
테스트 3 〉	통과 (0.01ms, 9.27MB)
테스트 4 〉	통과 (0.01ms, 9.2MB)
테스트 5 〉	통과 (0.03ms, 9.17MB)
테스트 6 〉	통과 (0.06ms, 9.27MB)
테스트 7 〉	통과 (2.01ms, 9.42MB)
테스트 8 〉	통과 (0.70ms, 9.28MB)
테스트 9 〉	통과 (3.63ms, 9.25MB)
테스트 10 〉	통과 (1.65ms, 9.34MB)
테스트 11 〉	통과 (3.74ms, 9.36MB)
테스트 12 〉	통과 (3.30ms, 9.33MB)
테스트 13 〉	통과 (0.21ms, 9.19MB)
테스트 14 〉	통과 (4.03ms, 9.33MB)
'''