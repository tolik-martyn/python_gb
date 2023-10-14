from random import randint

"""Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь
следующие методы:
• new_game() - для создания новой игры;
• get_field() - для получения поля (список списков);
• check_field() - для проверки, есть ли победитель, который
возвращает X, если
победил первый игрок, 0, если второй, D, если ничья и None, если можно
продолжать игру;
- make_move(row, col) - который устанавливает значение текущего хода в ячейку
поля с координатами row, col, если это возможно, «переключает» ход игрока, а
также возвращает сообщение «Победил игрок Х» при победе крестиков, «Победил
игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть»,
если победитель после данного хода неопределён.
Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже
занята», если в клетке уже стоит крестик или нолик, и «Игра уже завершена», если в
текущей игре уже выявлен победитель или закончились ячейки для ходов.
При создании объекта класса должна создаваться новая игра.
Аргументы row и col метода make_move могут принимать значения от 1 до 3."""


class TicTacToeBoard:

    def __init__(self):
        self.list_obj = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        print('Новая игра!')
        self.step = randint(0, 1)
        if self.step == 0:
            print('Первыми ходят нолики:')
        else:
            print('Первыми ходят крестики:')

    def new_game(self):
        self.list_obj = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        print('Новая игра!')
        self.step = randint(0, 1)
        if self.step == 0:
            print('Первыми ходят нолики:')
        else:
            print('Первыми ходят крестики:')

    def get_field(self):
        print('Актуальное поле:')
        print(*self.list_obj, sep='\n')

    def check_field(self):
        if (self.list_obj[0][0] == 'X' and self.list_obj[0][1] == 'X' and self.list_obj[0][2] == 'X')\
                or (self.list_obj[1][0] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[1][2] == 'X')\
                or (self.list_obj[2][0] == 'X' and self.list_obj[2][1] == 'X' and self.list_obj[2][2] == 'X')\
                or (self.list_obj[0][0] == 'X' and self.list_obj[1][0] == 'X' and self.list_obj[2][0] == 'X')\
                or (self.list_obj[0][1] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][1] == 'X')\
                or (self.list_obj[0][2] == 'X' and self.list_obj[1][2] == 'X' and self.list_obj[2][2] == 'X')\
                or (self.list_obj[0][0] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][2] == 'X')\
                or (self.list_obj[0][2] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][0] == 'X'):
            print('X')
        elif (self.list_obj[0][0] == '0' and self.list_obj[0][1] == '0' and self.list_obj[0][2] == '0')\
                or (self.list_obj[1][0] == '0' and self.list_obj[1][1] == '0' and self.list_obj[1][2] == '0')\
                or (self.list_obj[2][0] == '0' and self.list_obj[2][1] == '0' and self.list_obj[2][2] == '0')\
                or (self.list_obj[0][0] == '0' and self.list_obj[1][0] == '0' and self.list_obj[2][0] == '0')\
                or (self.list_obj[0][1] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][1] == '0')\
                or (self.list_obj[0][2] == '0' and self.list_obj[1][2] == '0' and self.list_obj[2][2] == '0')\
                or (self.list_obj[0][0] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][2] == '0')\
                or (self.list_obj[0][2] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][0] == '0'):
            print('0')
        elif '-' in self.list_obj[0] or '-' in self.list_obj[1] or '-' in self.list_obj[2]:
            print('None')
        else:
            print('D')

    def make_move(self, row, col):
        if row > 3 or col > 3 or row < 1 or col < 1:
            print(
                'Ход не засчитан, попробуйте еще раз (строка и столбец могут принимать значения от 1 до 3):')
        else:
            if self.list_obj[row - 1][col-1] == '0' or self.list_obj[row - 1][col-1] == 'X':
                print(
                    f'Ход не засчитан, попробуйте еще раз (клетка [{row}, {col}] уже занята»):')
            else:
                if self.step == 0:
                    self.list_obj[row - 1][col-1] = '0'
                    print(f'Ход ноликов: [{row}, {col}]')
                else:
                    self.list_obj[row - 1][col-1] = 'X'
                    print(f'Ход крестиков: [{row}, {col}]')

                if (self.list_obj[0][0] == 'X' and self.list_obj[0][1] == 'X' and self.list_obj[0][2] == 'X')\
                        or (self.list_obj[1][0] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[1][2] == 'X')\
                        or (self.list_obj[2][0] == 'X' and self.list_obj[2][1] == 'X' and self.list_obj[2][2] == 'X')\
                        or (self.list_obj[0][0] == 'X' and self.list_obj[1][0] == 'X' and self.list_obj[2][0] == 'X')\
                        or (self.list_obj[0][1] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][1] == 'X')\
                        or (self.list_obj[0][2] == 'X' and self.list_obj[1][2] == 'X' and self.list_obj[2][2] == 'X')\
                        or (self.list_obj[0][0] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][2] == 'X')\
                        or (self.list_obj[0][2] == 'X' and self.list_obj[1][1] == 'X' and self.list_obj[2][0] == 'X'):
                    print('Победили крестики!')

                elif (self.list_obj[0][0] == '0' and self.list_obj[0][1] == '0' and self.list_obj[0][2] == '0')\
                        or (self.list_obj[1][0] == '0' and self.list_obj[1][1] == '0' and self.list_obj[1][2] == '0')\
                        or (self.list_obj[2][0] == '0' and self.list_obj[2][1] == '0' and self.list_obj[2][2] == '0')\
                        or (self.list_obj[0][0] == '0' and self.list_obj[1][0] == '0' and self.list_obj[2][0] == '0')\
                        or (self.list_obj[0][1] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][1] == '0')\
                        or (self.list_obj[0][2] == '0' and self.list_obj[1][2] == '0' and self.list_obj[2][2] == '0')\
                        or (self.list_obj[0][0] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][2] == '0')\
                        or (self.list_obj[0][2] == '0' and self.list_obj[1][1] == '0' and self.list_obj[2][0] == '0'):
                    print('Победили нолики!')

                elif '-' in self.list_obj[0] or '-' in self.list_obj[1] or '-' in self.list_obj[2]:
                    print('Продолжаем играть!')
                    if self.step == 0:
                        self.step = 1
                        print('Следующий ход делают крестики:')
                    else:
                        self.step = 0
                        print('Следующий ход делают нолики:')

                else:
                    print('Ничья!')


board = TicTacToeBoard()
board.get_field()
board.make_move(1, 1)
board.get_field()
board.make_move(1, 1)
board.make_move(1, 2)
board.get_field()
board.make_move(2, 1)
board.make_move(2, 2)
board.make_move(3, 1)
board.make_move(2, 2)
board.get_field()
