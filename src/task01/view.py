def view_input1():
    text = input('\nВведите:\n' +
                 '0 - чтобы сделать запись\n' +
                 '1 - чтобы получить запись\n: ')
    return text


def view_input2():
    text = input('Введите:\n' +
                 '0 - чтобы выбрать "addresses.txt"\n' +
                 '1 - чтобы выбрать "departments.txt"\n' +
                 '2 - чтобы выбрать "positions.txt"\n' +
                 '3 - чтобы выбрать "emails.txt"\n' +
                 '4 - чтобы выбрать "phone_numbers.txt"\n' +
                 '5 - чтобы выбрать "staff.txt"\n: ')

    return text


def view_write(data):
    print(f'\nСделана запись:\n{", ".join(data)}')


def view_read(data):
    if len(data) == 1:
        print(f'\nНайдена запись:\n{data[0]}')
    elif len(data) > 1:
        print('\nНайдены записи:')
        for i in range(len(data)):
            print(data[i])
    else:
        print('\nЗаписи не найдены')
