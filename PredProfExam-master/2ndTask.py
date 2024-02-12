class Students:
    id = 0
    student_name = ''
    work_id = 0
    Class = ''
    score = 0


file_open_students = open('students.csv')
students = []
j = 0
skip = file_open_students.readline()


for i in file_open_students:
    s = i.split(',')
    if(int(s[3][:-1])) == 10:
        students.append(Students())
        students[j].student_name = s[1]
        students[j].score = int(s[4])
        j += 1


for i in range(len(students)):
    j = i
    t = students[i]
    while j > 0 and students[j - 1].score < t.score:
        students[j] = students[j - 1]
        j -= 1
    students[j] = t

print(f'10 класс')
print(f'1 место: {students[0].student_name.split()[1][0]}. {students[0].student_name.split()[0]}')
print(f'2 место: {students[1].student_name.split()[1][0]}. {students[1].student_name.split()[0]}')
print(f'3 место: {students[2].student_name.split()[1][0]}. {students[2].student_name.split()[0]}')

