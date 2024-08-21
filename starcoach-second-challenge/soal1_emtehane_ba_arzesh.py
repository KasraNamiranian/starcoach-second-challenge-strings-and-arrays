n = int(input())

students = []

for i in range(n):
    scores = list(map(int, input().split()))
    students.append((scores[0], scores[1], scores[2], i + 1))

students.sort(key=lambda x: (-x[0], -x[1], -x[2]))

result = [student[3] for student in students]

print(" ".join(map(str, result)))
