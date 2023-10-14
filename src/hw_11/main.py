class Auto:
    # атрибуты класса
    auto_name = "Lexus"
    auto_model = "RX 350L"
    auto_year = 2019

    # методы класса
    def on_auto_start(self):  # <self> - это ссылка на объект
        print(f"Заводим автомобиль")

    def on_auto_stop(self):
        print("Останавливаем работу двигателя")


a = Auto()

# print(a)  # <__main__.Auto object at 0x0000014267D90390>
# print(type(a))  # <class '__main__.Auto'>

# print(a.auto_name)  # Lexus (вывод через объект класса <a>)
# print(Auto.auto_name)  # Lexus (вывод через сам класс <Auto>)

a.on_auto_start()  # Заводим автомобиль. Методы запускаются с объектами, поэтому здесь не получится использовать <Auto> (как это было при auto_name)
a.on_auto_stop()  # Останавливаем работу двигателяА
