from random import randint, shuffle

def create_login(user: str) -> str:
    data_user = user.split(' ')
    return f'{data_user[0]}_{data_user[1][0]}{data_user[2][0]}'


def create_password() -> str:
    n_num = randint(1, 3)
    n_abc = randint(1, 2)
    n_ABC = randint(1, 3)
    n_char = 8 - n_abc - n_ABC - n_num
    num = [chr(randint(48, 57)) for _ in range(n_num)]
    abc = [chr(randint(97, 122)) for _ in range(n_abc)]
    ABC = [chr(randint(65, 90)) for _ in range(n_ABC)]
    chars = [chr(randint(33, 47)) for _ in range(n_char)]
    password = num + abc + ABC + chars
    shuffle(password)
    return ''.join(password)


def main():
    file_open_students = open('students.csv', encoding="utf8")
    file_redact_students = open('students_new.csv', 'w')
    students = []
    h = file_open_students.readline()
    for i in file_open_students.readlines():
        s = i.split(',')
        s.append(create_login(str(s[1])))
        s.append(create_password())
        students.append(s)

    r = 'id,Name,titleProject_id,class,score,login,password\n'
    for id, name, titleProject_id, klass, score, login, password in file_open_students:
        r += f'{id},{name},{titleProject_id},{klass},{score},{login},{password}'
        print(r)


    # file_redact_students.write(r)
    # file_redact_students.close()


if __name__ == '__main__':
    main()
