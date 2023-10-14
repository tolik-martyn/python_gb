"""Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом
отдельно чётные и нечётные. Числа добавляются в объект с помощью метода
add_number. Методы even и odd должны возвращать списки чётных и нечётных чисел
соответственно. Числа в списке должны идти в том же порядке, что и при добавлении в
объект."""


class OddEvenSeparator:

    def __init__(self):
        self.list_obj = []

    def add_num(self, num: int):
        self.list_obj.append(num)

    def even(self):
        return list(filter(lambda x: not x % 2, self.list_obj))

    def odd(self):
        return list(filter(lambda x: x % 2, self.list_obj))


x = OddEvenSeparator()
x.add_num(4)
x.add_num(3)
x.add_num(2)
x.add_num(1)

print(x.even())
print(x.odd())
