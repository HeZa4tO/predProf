from random import randint, shuffle
import csv


def create_login(user: str) -> str:
    """Функция генерации логина"""
    data_user = user.split(' ')
    return f'{data_user[0]}_{data_user[1][0]}{data_user[2][0]}'


def create_password() -> str:
    """Функция генерации пароля"""
    n_num = randint(1, 3)
    n_abc = randint(1, 3)
    n_ABC = randint(1, 3)
    n_char = 8 - n_abc - n_ABC - n_num
    num = [chr(randint(48, 57)) for _ in range(n_num)]
    abc = [chr(randint(97, 122)) for _ in range(n_abc)]
    ABC = [chr(randint(65, 90)) for _ in range(n_ABC)]
    chars = [chr(randint(33, 47)) for _ in range(n_char)]
    password = num + abc + ABC + chars
    shuffle(password)
    return ''.join(password)


def createLoginPassword():
    with open('students.csv', encoding="utf8") as file_open_students, open('students_new.csv', 'w', encoding="utf8", newline='') as file_redact_students:
        reader = csv.reader(file_open_students)
        writer = csv.writer(file_redact_students)
        students = []

        header = next(reader)   # Пропускаем заголовок
        header.extend(['login', 'password'])    # Добавление столбцов "login" и "password" в заголовок
        students.append(header)

        for row in reader:
            row.append(create_login(row[1]))
            row.append(create_password())
            students.append(row)

        writer.writerows(students)


if __name__ == '__main__':
    createLoginPassword()