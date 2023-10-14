import csv


def guide_ex_first():
    some_guide = []
    request = input('Введите данные для поиска: ')
    with open('guide.txt', 'r', encoding='utf-8') as file:
        some_list = file.read().splitlines()
        for i in range(len(some_list)):
            if request in some_list[i]:
                some_guide.append(some_list[i])

    return request, some_guide


def guide_ex_second():
    some_guide = []
    request = input('Введите данные для поиска: ')
    with open('guide.csv', 'r', encoding='utf-8') as file:
        some_list = list(csv.reader(file))
        for row in some_list:
            some_str = ''
            for i in range(len(row)):
                if request in row[i]:
                    for j in range(len(row)-1):
                        some_str += row[j] + ','
                    some_str += row[len(row)-1]
                    some_guide.append(some_str)
                    break

    return request, some_guide
