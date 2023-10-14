import msvcrt
import random

print('\n1. Задайте список из нескольких чисел. Напишите программу, ' +
      'которая найдёт сумму элементов списка, стоящих на нечётной позиции.' +
      '\nПример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12' +
      '\nРешение:')

size = int(input('Введите размер списка: '))
some_list = []
summ = 0

for i in range(size):
    some_list.append(random.randint(0, 9))
    if i % 2 == 1:
        summ += some_list[i]

print(
    f'Вывод списка -> {some_list}\nСумма элементов на нечетных позициях -> {summ}')


msvcrt.getch()
print('\n2. Напишите программу, которая найдёт произведение пар чисел списка. Парой ' +
      'считаем первый и последний элемент, второй и предпоследний и т.д.\nПримеры:' +
      '\n[2, 3, 4, 5, 6] => [12, 15, 16];\n[2, 3, 5, 6] => [12, 15]' +
      '\nРешение:')

size1 = int(input('Введите размер списка: '))
some_list1 = []

for i in range(size1):
    some_list1.append(random.randint(1, 9))
print(f'Вывод списка -> {some_list1}')

if size1 % 2 == 1:
    size2 = size1 // 2 + 1
else:
    size2 = size1 // 2

some_list2 = []

for i in range(size2):
    some_list2.append(some_list1[i] * some_list1[-1 - i])
print(f'Вывод произведения пар чисел списка -> {some_list2}')


msvcrt.getch()
print('\n3. Задайте список из вещественных чисел. Напишите программу, которая найдёт ' +
      'разницу между максимальным и минимальным значением дробной части элементов.' +
      '\nПример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19' +
      '\nРешение:')

size = int(input('Введите размер списка: '))
some_list = []

minn = 1
maxx = 0

for i in range(size):
    some_list.append(round(random.randint(1, 9) * random.random(), 2))
    if some_list[i] % 1 < minn and some_list[i] % 1 != 0:
        minn = round(some_list[i] % 1, 2)
    if some_list[i] % 1 > maxx:
        maxx = round(some_list[i] % 1, 2)

print(f'Вывод списка -> {some_list}\nРазница между максимальным [{maxx}] и ' +
      f'минимальным [{minn}] значением дробной части элементов -> {round(maxx - minn,2)}.')


msvcrt.getch()
print('\n4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.' +
      '\nПримеры:\n45 -> 101101\n3 -> 11\n2 -> 10\nРешение:')

ten = int(input('Введите десятичное число: '))
cur_ten = ten
two = ""

while cur_ten > 0:
    two = str(cur_ten % 2) + two
    cur_ten //= 2

print(f'Десятичное число {ten} в двоичной системе -> {two}')


msvcrt.getch()
print('\n5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.\nПример:' +
      '\nдля k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]\nРешение:')

num = int(input('Введите число: '))
size = num + 1

some_list = []

fib = 0
some_list.append(fib)
some_list.append(fib+1)
some_list.insert(0, fib+1)

for i in range(2, size):
    if i % 2 == 0:
        some_list.append(some_list[-1] + some_list[-2])
        some_list.insert(0, -some_list[-1])
    else:
        some_list.append(some_list[-1] + some_list[-2])
        some_list.insert(0, some_list[-1])

print(some_list)
