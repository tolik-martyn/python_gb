def write_address():
    list0 = [input('Введите ID нового адреса: '),
             input('Введите название города: '),
             input('Введите название улицы: '),
             input('Введите номер дома: '),
             input('Введите номер корпуса/строения: '),
             input('Введите номер квартиры: ')]

    with open('addresses.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0


def write_department():
    list0 = [input('Введите ID нового отдела: '),
             input('Введите название отдела: ')]

    with open('departments.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0


def write_position():
    list0 = [input('Введите ID новой должности: '),
             input('Введите название должности: '),
             input('Введите размер оклада: ')]

    with open('positions.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0


def write_email():
    list0 = [input('Введите ID нового e-mail: '),
             input('Введите название e-mail: ')]

    with open('emails.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0


def write_phone_number():
    list0 = [input('Введите ID нового телефона: '),
             input('Введите номер телефона: ')]

    with open('phone_numbers.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0


def write_staff():
    list0 = [input('Введите ID нового сотрудника: '),
             input('Введите фамилию: '),
             input('Введите имя: '),
             input('Введите отчество: '),
             input('Введите дату рождения: '),
             input('Введите ID должности: '),
             input('Введите ID отдела: '),
             input('Введите ID телефона: '),
             input('Введите ID e-mail: '),
             input('Введите ID адреса: ')]

    with open('staff.txt', 'a', encoding='utf-8') as file:
        file.write(f'{", ".join(list0)}\n')

    return list0
