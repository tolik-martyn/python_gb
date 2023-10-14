import msvcrt
import random


print('\n1.1. Напишите программу, удаляющую из текста все слова, содержащие "абв".' +
      '\nРешение:')

some_text1 = 'аабвпит заабвди апщилзп плибтпзл птопт пзщотзп хъоабввхт щптзт ахиабвьжим пдлтпт'
print(f'Начальный список: {some_text1}')

some_list1 = list(
    filter(lambda i: 'абв' not in i, some_text1.split()))

print(f'Итоговый список: {some_list1}')


msvcrt.getch()
print('\n1.2. Напишите программу, удаляющую из текста все слова, содержащие "а", "б", "в".' +
      '\nРешение:')

some_text2 = 'аабвпит заабвди апщилзп плибтпзл птаопт пзщотзп хъоабввхт щптввзт ахиабвьжим пдлтпт'
print(f'Начальный список: {some_text2}')

some_list2 = list(
    filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, some_text2.split()))

print(f'Итоговый список: {some_list2}')


msvcrt.getch()
print('\n2. Создайте программу для игры в "Крестики-нолики"'
      '\nРешение:')


def hod(j, some_list):
    step = (int(input('Введите позицию строки (от 1 до 3): ')),
            int(input('Введите позицию столбца (от 1 до 3): ')))
    if j == 0:
        some_list[step[0]-1][step[1]-1] = '0'
    else:
        some_list[step[0]-1][step[1]-1] = 'X'

    return some_list


def game(i, s_list, count):

    if count < stop:
        if i == 0:
            print('\nХод ноликов')
            hod(i, s_list)
            for el in s_list:
                print(el)
            win(i, s_list)
            if win(i, s_list) == 0:
                print('Выйграли нолики')
                return
            count += 1
            game(1, s_list, count)
        else:
            print('\nХод крестиков')
            hod(i, s_list)
            for el in s_list:
                print(el)
            if win(i, s_list) == 1:
                print('Выйграли крестики')
                return
            count += 1
            game(0, s_list, count)
    else:
        return print('Ничья')


def win(i, so_list):
    if i == 0:
        k = '0'
    else:
        k = 'X'

    if (so_list[0][0] == k and so_list[0][1] == k and so_list[0][2] == k) \
            or (so_list[1][0] == k and so_list[1][1] == k and so_list[1][2] == k)\
            or (so_list[2][0] == k and so_list[2][1] == k and so_list[2][2] == k)\
            or (so_list[0][0] == k and so_list[1][0] == k and so_list[2][0] == k)\
            or (so_list[0][1] == k and so_list[1][1] == k and so_list[2][1] == k)\
            or (so_list[0][2] == k and so_list[1][2] == k and so_list[2][2] == k)\
            or (so_list[0][0] == k and so_list[1][1] == k and so_list[2][2] == k)\
            or (so_list[0][2] == k and so_list[1][1] == k and so_list[2][0] == k):
        if i == 0:
            return 0
        else:
            return 1
    else:
        return


som_list = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
count = 0
stop = 9


whose_hod = random.randint(0, 1)
print(f'Первый ход: {whose_hod}')

if whose_hod == 0:
    game(0, som_list, count)
else:
    game(1, som_list, count)


msvcrt.getch()
print('\n3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.' +
      '\nВходные и выходные данные хранятся в отдельных текстовых файлах.'
      '\nРешение:')

text1 = 'Для вас, души моей царицы,\n\
Красавицы, для вас одних\n\
Времен минувших небылицы,\n\
В часы досугов золотых,\n\
Под шепот старины болтливой,\n\
Рукою верной я писал;\n\
Примите ж вы мой труд игривый!\n\
Ничьих не требуя похвал,\n\
Счастлив уж я надеждой сладкой,\n\
Что дева с трепетом любви\n\
Посмотрит, может быть, украдкой\n\
На песни грешные мои.'


def compres(some_str):
    alphabet = set(some_str)
    some_list4 = []
    for i in alphabet:
        some_list3 = []
        for j in range(0, len(some_str)):
            if i == some_str[j]:
                some_list3.append(j)
        some_list4.append(tuple([i, some_list3]))
    return some_list4


with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(f'{compres(text1)}')

with open('file.txt', 'r', encoding='utf-8') as file:
    some_list5 = file.read()

text2 = [''] * len(text1)

some_list5 = some_list5.replace(
    '[(', '', 1).replace(')]', '', 1).replace(']', '').replace("'", '').split('), (')


for i in range(0, len(some_list5)):
    some_list5[i] = some_list5[i].split(', [')
    some_list5[i][1] = some_list5[i][1].split(', ')
    for j in some_list5[i][1]:
        text2[int(j)] = some_list5[i][0]

print(*text2, sep='')
