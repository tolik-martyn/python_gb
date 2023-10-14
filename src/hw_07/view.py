def choice():
    some_str = input(
        '\nВведите "0" (чтобы сделать запись в справочнике), или введите "1" (чтобы получить запись из справочника): ')
    return some_str


def view_data_im(data):
    if len(data) == 4:
        print(f'\nСоздана запись:')
        print(f'*{", ".join(data)}')
    else:
        print(f'\nСозданы записи:')
        for i in data:
            print(f'*{", ".join(i)}')


def view_data_ex(request, data):
    if len(data) == 1:
        print(f'\nПо запросу "{request}" получена запись:')
        print(f'*{", ".join(data)}')
    elif len(data) > 1:
        print(f'\nПо запросу "{request}" получены записи:')
        for i in data:
            print(f'*{i}')
    else:
        print(f'\nПо запросу "{request}" записи не найдены')
