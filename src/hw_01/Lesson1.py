import math
import msvcrt

print('\n1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.' +
      '\nПример:\n6 -> да\n7 -> да\n1 -> нет')

number = int(input('Введите день недели: '))

if number > 5 and number < 8:
    print('Выходной день')
elif number > 0 and number < 6:
    print('Будний день')
else:
    print('День недели введен неверно')

msvcrt.getch()


print('\n2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            truth = (not (x or y or z)) == (not (x) and not (y) and not (z))
            print(f'[x: {x}, y: {y}, z: {z}] -> {truth}')

msvcrt.getch()


print('\n3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 ' +
      'и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).' +
      '\nПример:\n- x=34; y=-30 -> 4\n- x=2; y=4-> 1\n- x=-34; y=-30 -> 3')

number_x = int(input('Введите X: '))
number_y = int(input('Введите Y: '))

if number_x > 0 and number_y > 0:
    print('1 четверть')
elif number_x < 0 and number_y > 0:
    print('2 четверть')
elif number_x < 0 and number_y < 0:
    print('3 четверть')
elif number_x > 0 and number_y < 0:
    print('4 четверть')
elif number_x == 0 and number_y != 0:
    print('Точка лежит на оси X')
elif number_x != 0 and number_y == 0:
    print('Точка лежит на оси Y')
else:
    print('Точка лежит в центре оси координат')

msvcrt.getch()


print('\n4. Напишите программу, которая по заданному номеру четверти, показывает диапазон ' +
      'возможных координат точек в этой четверти (x и y).')

number = int(input('Введите номер четверти: '))

if number == 1:
    print('x > 0; y > 0')
elif number == 2:
    print('x < 0; y > 0')
elif number == 3:
    print('x < 0; y < 0')
elif number == 4:
    print('x > 0; y < 0')
else:
    print('Номер четверти введен неверно')

msvcrt.getch()


print('\n5. Напишите программу, которая принимает на вход координаты двух точек и находит ' +
      'расстояние между ними в 2D пространстве.' +
      '\nПример:\n- A (3,6); B (2,1) -> 5,09\n- A (7,-5); B (1,-1) -> 7,21')

print('Введите координаты точки A:')
xa = int(input('xA: '))
ya = int(input('yA: '))

print('Введите координаты точки B:')
xb = int(input('xB: '))
yb = int(input('yB: '))

distance = math.sqrt((xb-xa)**2 + (yb - ya)**2)

print(f'Расстояние между точкой А и B -> {round(distance, 3)}')
