import csv


def guide_im_first():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите телефон: ')
    comment = input('Введите описание: ')
    some_list = [last_name, first_name, phone_number, comment]

    with open('guide.txt', 'a', encoding='utf-8') as file:
        file.write(f'{last_name},{first_name},{phone_number},{comment}\n')

    return some_list


def guide_im_second():
    some_list = []
    exit = False
    while not exit:
        some_list.append([input('Введите фамилию: '), input('Введите имя: '), input(
            'Введите телефон: '), input('Введите описание: ')])
        some_exit = input(
            'Введите "да" (чтобы сделать ещё одну запись), или любой другой текст (чтобы остановить ввод): ')
        if some_exit != 'да':
            exit = True
    with open('guide.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in some_list:
            writer.writerow(row)

    if len(some_list) == 1:
        return some_list[0]
    else:
        return some_list
