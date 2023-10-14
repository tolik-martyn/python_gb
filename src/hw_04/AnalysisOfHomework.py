import msvcrt
import math
import sympy
import random


# ---------------------------------------------------------------------

print('\n1. Вычислите число c заданной точностью d.\nПример:' +
      '\nпри d = 0.001, π = 3.141\n10^{-1} ≤ d ≤ 10^{-10}' +
      '\nРешение:')

d = input()
accur = len(d)
print(str(math.pi)[0:accur])


# ---------------------------------------------------------------------


print('\n2. Задайте натуральное число N. Напишите программу, которая ' +
      'составит список простых множителей числа N.' +
      '\nРешение:')

n = int(input())
some_list = []
for i in range(1, n + 1):
    if n % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            some_list.append(i)
print(*some_list, sep=', ')


# ---------------------------------------------------------------------


print('\n3. Задайте последовательность чисел. Напишите программу, которая выведет ' +
      'список неповторяющихся элементов исходной последовательности.' +
      '\nРешение:')

# Первое решение:

number_set = set()
out_list = []
some_list = list(map(int, input().split()))
for ind in range(0, len(some_list)):
    if some_list[ind] not in number_set:
        number_set.add(some_list[ind])
        for ind1 in range(ind + 1, len(some_list)):
            if some_list[ind] == some_list[ind1]:
                break
        else:
            out_list.append(some_list[ind])
print(out_list)


# Второе решение:

some_list = list(map(int, input().split()))
for i in some_list:
    if some_list.count(i) == 1:
        print(i, end=' ')


# ---------------------------------------------------------------------
