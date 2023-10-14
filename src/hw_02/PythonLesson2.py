import random
import msvcrt

print('\n1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.' +
      '\nПример:\n- 6782 -> 23\n- 0,56 -> 11')

sum = 0
number = input('Введите число: ')
for i in number:
    if i != ',' and i != '.':
        sum += int(i)
print(f'Сумма цифр числа {number} -> {sum}')


msvcrt.getch()
print('\n2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.' +
      '\nПример:\n- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)')

number = int(input('Введите число N: '))
multi = 1
list = []
for i in range(1, number + 1):
    multi *= i
    list.append(multi)
print(f'Набор произведений чисел от 1 до {number} -> {list}')


msvcrt.getch()
print('\n3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.' +
      '\nПример:\n- Для n = 4 -> (1: 2, 2: 2.25, 3: 2.37, 4: 2.44)\nСумма -> 9.06')

number = int(input('Введите число n: '))
sum = 0
dictionary = {}
for i in range(1, number + 1):
    dictionary[i] = round((1 + 1 / i) ** i, 2)
    sum += dictionary[i]
print(f'Для n = {number} список -> {dictionary}\nСумма -> {sum}')


msvcrt.getch()
print('\n4. Реализуйте алгоритм перемешивания списка.')

list = []
n = int(input('Введите размер списка: '))

for i in range(n):
    list.append(random.randint(0, 99))
print(f'Первоначальный список -> {list}')

random.shuffle(list)
print(f'Перемешанный список -> {list}')
