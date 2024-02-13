# Сортировка Вставками:

for i in range(len(students)):
    j = i
    t = students[i]
    while j > 0 and students[j - 1].score < t.score:
        students[j] = students[j - 1]
        j -= 1
    students[j] = t


# Сортировка Пузырьком (с флажком):

f = True
while f:
    f = False
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            f = True
            a[j], a[j+1] = a[j+1], a[j]


# Сортировка Пузырьком

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


# Сортировка Выбором:

for i in range(len(a))
    m = i
    for j in range(i, len(a)):
        if a[j] < a[m]:
            m = j
    a[i], a[m] = a[m], a[i]

