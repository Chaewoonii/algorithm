# 359p, q23-국영수, 정렬

n = int(input())
students = []

for _ in range(n):
    studentInfo = input().split()
    students.append([studentInfo[0], int(studentInfo[1]), int(studentInfo[2]), int(studentInfo[3])])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
