def read_address():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID адреса\n' +
                        '1 - для вывода по названию города\n' +
                        '2 - для вывода по названию улицы\n' +
                        '3 - для вывода по номеру дома\n' +
                        '4 - для вывода по номеру корпуса/строения\n' +
                        '5 - для вывода по номеру квартиры\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('addresses.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1


def read_department():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID отдела\n' +
                        '1 - для вывода по названию отдела\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('departments.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1


def read_position():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID должности\n' +
                        '1 - для вывода по названию должности\n' +
                        '2 - для вывода по размер оклада\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('positions.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1


def read_email():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID e-mail\n' +
                        '1 - для вывода по названию e-mail\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('emails.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1


def read_phone_number():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID телефона\n' +
                        '1 - для вывода по номеру телефона\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('phone_numbers.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1


def read_staff():
    list1 = []
    search1 = int(input('Введите:\n' +
                        '0 - для вывода по ID сотрудника\n' +
                        '1 - для вывода по фамилии\n' +
                        '2 - для вывода по имени\n' +
                        '3 - для вывода по отчеству\n' +
                        '4 - для вывода по дате рождения\n' +
                        '5 - для вывода по ID должности\n' +
                        '6 - для вывода по ID отдела\n' +
                        '7 - для вывода по ID телефона\n' +
                        '8 - для вывода по ID e-mail\n' +
                        '9 - для вывода по ID адреса\n: '))
    search2 = input('Введите данные для поиска: ')
    with open('staff.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().splitlines()
        for i in range(len(list0)):
            if search2.lower() in list0[i].split(', ')[search1].lower():
                list1.append(list0[i])
    return list1
