class Auto:
    # атрибуты класса
    # <auto_count> будет типа счетчика. Для вывода использовать <print(Auto.auto_count)>
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto()
a.on_auto_start('Audi', 'RS6', 2019)
b = Auto()
b.on_auto_start('BMW', 'M5', 2020)
print(a.auto_name)
print(b.auto_year)
