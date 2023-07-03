student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
avg = 0

for n in student_heights:
    total += n

for n in student_heights:
    avg += 1

print(round(total / avg))
