"""Напишите класс BigBell, который при вызове метода sound печатает попеременно слова
ding и dong, начиная с ding."""


class BigBell:

    def __init__(self):
        self.flag = True

    def sound(self):
        if self.flag:
            print("ding")
            self.flag = False
        else:
            print("dong")
            self.flag = True


x = BigBell()
x.sound()
x.sound()
x.sound()
