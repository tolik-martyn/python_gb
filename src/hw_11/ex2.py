"""Напишите класс кнопки Button, экземпляры которого будут измерять количество
нажатий на кнопку-объект.
Метод click увеличивает количество нажатий, метод click_count возвращает число
нажатий. Метод reset обнуляет количество нажатий."""


class Button:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0


button = Button()
button.click()
button.click()
print(button.click_count())
button.click()
print(button.click_count())
b = Button()
print(b.click_count())
